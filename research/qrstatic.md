# QR Static — Research Notes

> Raw research on the QR static steganography family. Not published. Three repositories, one concept, a decisive design pivot. Based on full source-level analysis by five parallel agents covering every `.py` and `.rs` file across all three repos.

## Repositories

| Repository | Language | Commits | Active dates | LOC | Role |
|---|---|---|---|---|---|
| `qr-static-stream` | Python | 13 | Dec 18, 2025 (+1 Feb 3, 2026) | 4,538 | Original prototype |
| `qrstatic` | Rust | 46 | Mar 15–16, 2026 (+1 May 1) | 14,647 | Production rewrite |
| `qrstatic-riptide` | Rust | 11 | Mar 27, 2026 (+1 May 1) | 6,002 | Naive-accumulation reference port |

All three pursue the same concept: hide a QR code inside a sequence of noise-like frames such that the QR is latent in the carrier sequence and only emerges under the correct recovery procedure.

## Chronology

### Dec 18, 2025 — Python prototype (all in one day)

`qr-static-stream` was built in a single session. 12 of 13 commits landed between 08:59 and 10:48. The session produced seven codec variants, each in its own file with a companion demo. Dependencies: NumPy, OpenCV (`cv2.QRCodeDetector`), the `qrcode` Python library. No from-scratch primitives — QR generation and detection are delegated to libraries.

The prototype was exploratory: breadth over rigor. Source analysis reveals significant bugs (documented below) that the README doesn't mention.

### Mar 15–16, 2026 — Production Rust rewrite (two days)

`qrstatic` was built across two concentrated days. 44 of 46 commits landed between 21:47 on March 15 and 18:50 on March 16. The two-day arc:

**Day 1 (Mar 15, evening):** Foundational primitives and experimental codecs. Phases 1–5 in sequence — grid, SHA-256, PRNG, bits, QR codec, then XOR, signed, and binary codecs. Hygiene ratchet added same night.

**Day 2 (Mar 16, morning–afternoon):** Documentation, CLI, then the design pivot. At 12:15 the temporal codec's prior-art grounding was documented. By 12:54, Stage 1 temporal was implemented. The rest of the afternoon tuned the baseline, added Stage 2 packet slice, the tiled transport prototype, two debug viewers, and the eval harnesses.

### Mar 27, 2026 — Riptide reference port (one day)

`qrstatic-riptide` was built 11 days after the production repo. 10 of 11 commits landed between 16:04 and 17:16. Riptide is the naive-accumulation design ported cleanly to zero-dependency Rust — the "before" state preserved alongside the production temporal codec. The shared May 1 dependency-policy commit across both Rust repos confirms coordinated maintenance.

## The Concept

The core idea is constant across all three repos:

1. Encode a message into a QR matrix.
2. Split the QR into N noise-like frames using a codec and a key.
3. Transmit the frames — each individually looks like random static.
4. Apply the correct recovery procedure to reconstruct the QR.
5. Decode the QR back to the original message.

The divergence is in step 4: what the recovery procedure is, and whether an attacker can bypass it.

## Python Prototype — Source Analysis

### Shared infrastructure

All seven Python codecs share infrastructure through copy-paste, not shared modules. `generate_qr_matrix`, `scan_qr`, `_pad_matrix`/`_resize_qr_to_frame`, and `_seed_to_rng`/`_frame_rng` are duplicated across 6 of 7 files (audio imports from binary instead). Divergence has already occurred:

- Threshold uses `<=` in analog/layered/signed/sliding but `<` in binary.
- `_pad_matrix` zero-pads; `_resize_qr_to_frame` scales by integer repeat then pads.
- `_seed_to_rng` uses `SHA-256(seed)[:8]` little-endian → `np.random.default_rng`. No KDF, no salt, no stretching — trivially brute-forceable for short seeds.

There are zero test files. Only demos validate behavior, and demos print rather than assert.

### Codec-by-codec findings

#### 1. XOR (`qr_static.py`)

N-1 random binary frames + one computed frame. XOR all N to recover the QR. Lossless, deterministic. No payload capacity. The streaming encoder has a convoluted defect: it re-seeds frames 0..N-2 with the encoder's own RNG, discarding whatever `encode()` produced (lines 187–189). Functionally correct but needlessly complex.

#### 2. Analog (`qr_static_analog.py`)

Float signal + noise. Signal: `±(signal_strength ± magnitude_bias) / N` per frame. Noise: uniform `[-amplitude, amplitude]`. QR recovered by thresholding accumulated sum at 0.

Payload hiding: ±0.5 magnitude bias on `signal_strength`. Payload decode regenerates the exact noise sequence using `_seed_to_rng(qr_seed)` and subtracts it. This works only because noise is deterministically seeded from the QR content, and the decoder recovers the QR first. The tight coupling between encode/decode RNG consumption order is the dominant fragility across all noise-cancellation codecs.

**Bug:** The decoder assumes the encoder consumed the RNG in frame order with identical parameters. Any parameter drift silently corrupts payload decoding.

#### 3. Binary (`qr_static_binary.py`)

Pure ±1 frames. QR emerges statistically. Each cell sampled as +1 with probability `base_bias` (white) or `1 - base_bias` (black). Payload modulates bias ±`payload_bias_delta`.

**Crucially different from analog:** the decoder does NOT regenerate or subtract noise. It relies purely on statistical expectation + majority voting. Simpler and more robust, but requires many frames.

**Bug:** The streaming encoder ignores payload — `bias_map` is computed without payload modulation (line 258). Batch and streaming APIs are inconsistent.

#### 4. Layered (`qr_static_layered.py`)

Two QR codes nested. `n1 × n2` total frames. Every `n1` frames accumulates to one L1 output. `n2` L1 outputs accumulate (after removing L1 signal) to reveal L2.

**Bug:** `layer2_signal` defaults to `2.0` in encode (line 101) but `3.0` in `decode_layer2_payload` (line 274). If a caller uses defaults directly, the threshold is wrong.

**Bug:** The streaming encoder pre-encodes all frames eagerly in `set_message()` (line 449), then dishes them out one at a time. This defeats the purpose of streaming — full O(n1·n2) memory.

#### 5. Sliding (`qr_static_sliding.py`)

L1 signal is identical per frame regardless of window position, so any `n1` consecutive frames decode the QR. L2 is additive overlay.

**Bug:** `apply_l2_overlay` applies L2 only to the first `total_l2_frames` frames (line 238); beyond that, pure noise. This creates a detectable boundary, undermining the "no boundaries" claim in the README.

**Bug:** The streaming decoder lacks L2 support entirely. L2 decode is batch-only.

**Bug:** `decode_l2` accepts a `stride` parameter but ignores it (line 321 comment).

#### 6. Signed (`qr_static_signed.py`)

First N-1 frames are pure RNG noise. The final frame is computed deterministically per-pixel to force correct sign. Payload encoded in magnitude via signal_strength multiplier.

**Critical bug:** The encoder consumes RNG for frames 0..N-2 (N-1 draws), but `_generate_expected_accumulation` consumes N draws. The RNG streams are misaligned by one frame. The "expected" noise does not match actual noise. Payload decoding is likely unreliable by design.

**Second issue:** The final frame correction can only contribute ±1 per cell. The `desired_magnitude` arithmetic computes a target but clamps to `sign(needed)`, making magnitude control largely decorative.

#### 7. Audio (`qr_static_audio.py`)

Sign-flipping, not additive offset. Cover audio samples have their signs flipped with probability `flip_probability` when they disagree with the desired QR sign. No payload. No noise cancellation.

**Performance:** Per-sample Python loop in `encode_audio` — catastrophically slow for real audio (1.3M iterations for 30s at 44100 Hz).

### Python prototype summary

The prototype's value was exploratory breadth. Seven codecs explored the design space from information-theoretic security (XOR) through statistical recovery (binary, audio) to recursive key-layering (layered, sliding). The bugs and fragilities were acceptable for a research prototype — but they motivated the Rust rewrite's emphasis on determinism, zero dependencies, and the hygiene ratchet.

## Riptide — Source Analysis

Riptide is the faithful naive-accumulation port to zero-dependency Rust. It preserves the Python prototype's six codec concepts (xor, accumulator, biased, windowed, multilayer, audio) on a from-scratch primitive stack.

### Primitive stack

**SHA-256** (`crypto/sha256.rs`): Textbook FIPS 180-4. `K` and `H_INIT` are `const` arrays. Single-shot only — allocates `Vec<u8>` for padding. Three NIST test vectors verify correctness.

**PRNG** (`crypto/prng.rs`): SHA-256 counter mode. `PRNG(state) = SHA256(seed || counter_le64)`. Per-frame seed derivation: `SHA256(master_key || frame_index_le32)`. This is the determinism guarantee — encoder and decoder derive identical noise for the same `(key, frame_index)` pair.

**GF(2⁸)** (`qr/galois.rs`): Primitive polynomial `0x11D`. Both `EXP[512]` (doubled to avoid modulo) and `LOG[256]` tables are `const fn`-evaluated at compile time. Full field operations: `mul`, `div`, `inv`, `pow`. Tests exhaustively verify 65K iteration round-trip property (`a*b/b == a`) for all nonzero elements.

**Reed-Solomon** (`qr/reed_solomon.rs`): Full encoder + decoder. Generator polynomial construction, systematic encoding via polynomial long division. Decoder pipeline: syndromes → Berlekamp-Massey → Chien search → Forney algorithm. The formal derivative exploits characteristic-2 (drops even-indexed terms). Tests verify zero-syndrome property, boundary error counts (t and t+1), and known reference codewords.

**QR codec** (`qr/`): Versions 1–10, all four ECC levels. Full encode pipeline: byte mode bitstream, RS block interleaving, matrix construction (finder/timing/alignment patterns, zigzag data placement), 8 mask patterns with 4-rule penalty scoring, BCH format info. Full decode pipeline: format info reading (both redundant copies), unmasking, reverse zigzag, de-interleave, RS decode, bitstream parse.

### Codec trait system

Three dyn-compatible traits: `Codec` (main interface), `StreamEncoder`/`StreamDecoder` (streaming state machines), `PayloadCodec` (supertrait for hidden payloads). The `Frame` type is a newtype over `Vec<Vec<i32>>` — `i32` accommodates all codec sample ranges uniformly.

### Codec improvements over Python

- **Windowed codec** contains a 130-line comment block documenting failed approaches before settling on the periodic XOR construction. This design-journey documentation is exceptional.
- **Audio codec** uses DSSS with per-bit PN chip sequences, a conceptual advance over the Python sign-flipping approach.
- **Multilayer codec** uses a peeling decoder that depends on exact PRNG reconstruction. Since the Rust PRNG is deterministic, this is exact — no approximation error propagates, unlike the Python version's fragile RNG coupling.

### What riptide lacks

No temporal codec. No spatial permutation. No detector-score gating. The signal lives in the per-frame mean in every codec — the same vulnerability all Python codecs share.

## Production Repo — Primitive Stack

The production repo's primitive stack is a refinement of riptide's. Key engineering differences:

### Grid

`Grid<T>` uses a single flat `Vec<T>` with row-major indexing (`row * width + col`). This is a structural improvement over riptide's `Vec<Vec<i32>>`: one allocation, contiguous memory, cache-friendly accumulation. The `accumulate_i16` and `accumulate_f32` methods are the hot path — every analog/signed/binary codec calls one.

### GF(256)

Same polynomial (`0x11D`), but the production version packages tables in a `Gf256Tables` struct with a static `TABLES` instance. The `mul` operation avoids the `% 255` modulo by relying on the 512-entry exp table having two full copies of the 255-element cycle. Since `log_a + log_b` maxes at 508 < 512, the lookup is always in bounds. This removes a division per multiply.

### PRNG

Xoshiro256** (double-star variant) instead of riptide's SHA-256 counter mode. State is `[u64; 4]`. Seeded by SHA-256 of a domain-separated string via `from_key(key, index)` which composes `format!("{key}:{index}")` before hashing.

Domain separation is achieved entirely through string prefixes embedded in the key: `"layer1:{layer1_key}"`, `"qrstatic:temporal:v1:l1:{master_key}:cell:{cell_idx}"`, etc. This prevents cross-codec PRNG stream collisions.

### QR codec

Narrower scope than riptide: versions 1–6 only (not 1–10), EC level H only (not all four levels), byte mode only. But the decoder has a noise-tolerance test (flips ~5% of data modules, confirms EC-H recovery) that riptide lacks.

The format info decoder uses brute-force nearest-codeword: tries all 32 valid format info values, computes Hamming distance, accepts if ≤3 errors. Simpler than implementing a BCH decoder, practical because the search space is tiny.

### Error model

Four-variant `Error` enum with no source chaining. The hygiene ratchet enforces zero `.unwrap()`, zero `.expect()`, one `panic!` (an impossible-case fallback in mask pattern matching). All errors propagate via `Result`. This is stricter than riptide, which uses `assert!` for preconditions.

### Hygiene ratchet

The `hygiene.rs` test recursively scans all `src/*.rs` files, strips inline test modules, then counts panic-inducing patterns:

| Pattern | Max allowed |
|---|---|
| `.unwrap()` | 0 |
| `.expect(` | 0 |
| `panic!(` | 1 |
| `unreachable!(` | 0 |
| `todo!(` | 0 |
| `unimplemented!(` | 0 |

This is a ratchet: budgets can only decrease. Adding any `.unwrap()` to production code fails CI. Test code is exempt because `#[cfg(test)]` modules are stripped before counting.

## Production Repo — Experimental Codecs

Seven experimental codecs preserved as research predecessors. Unlike riptide's trait-based system, the production repo uses concrete types per codec with a shared `Frame` enum and `EncodeConfig` struct — no dyn-dispatch traits.

Key implementation advances over riptide:

### Spatial permutation (binary codec)

The binary codec generates a deterministic Fisher-Yates shuffle keyed by `"qrstatic-binary-permutation:{w}x{h}"`. The QR bias map is computed in logical layout, then permuted to physical layout before frame sampling. This scrambles spatial correlation between cells so individual frames don't leak the QR pattern. This is a direct precursor to the temporal codec's per-frame spatial permutation.

### Signed codec payload

Payload bits are spread across cells via `idx % bits.len()`. Cells where the payload bit is 1 get `desired_magnitude += 2`. A Fisher-Yates shuffle (seeded per-cell) randomly assigns which frames get +1 vs -1, preventing per-frame leakage of the QR structure.

### Streaming

All codecs have streaming encoder/decoder state machines with `VecDeque` message queues and `push_frame`/`next_frame` interfaces. Riptide's codecs are batch-only.

### Universal QR recovery

`extract_qr_from_sign_grid` brute-forces all 6 QR sizes (21, 25, 29, 33, 37, 41), crops, attempts decode, returns first valid. This is how every codec recovers the hidden QR without knowing the version a priori.

## The Temporal Codec — Source Analysis

This is the production codec. The design correction that separates it from everything before it.

### The core insight

Every prior codec, in both Python and Rust, embeds the QR signal in the per-frame mean image. Accumulate enough frames and the signal emerges. The temporal codec moves the signal into keyed temporal correlation — a dimension that naive accumulation cannot access by construction.

### Chip schedule generation — the balance guarantee

The balance is enforced structurally, not probabilistically. For each cell, the code creates a vector with exactly `n_frames/2` copies of `+1.0` and exactly `n_frames/2` copies of `-1.0`, then applies a Fisher-Yates shuffle:

```rust
let mut chips = vec![1.0f32; n_frames / 2];
chips.extend(vec![-1.0f32; n_frames / 2]);
let mut rng = Prng::from_str_seed(
    &format!("qrstatic:temporal:v1:{domain}:{master_key}:cell:{cell_idx}")
);
for idx in (1..chips.len()).rev() {
    let swap_idx = (rng.next_u64() as usize) % (idx + 1);
    chips.swap(idx, swap_idx);
}
```

The shuffle permutes the order but cannot change the counts. For every cell, across the full window, the sum of chips is exactly `0.0`. When you sum frames without the key, the signal contributions self-cancel. This is verified by unit test.

`n_frames` must be even — the constructor rejects odd counts.

### Spatial permutation — per-frame, keyed, full shuffle

A full Fisher-Yates shuffle over all `width × height` cells, deterministic per `(master_key, frame_index)`:

```rust
let mut rng = Prng::from_str_seed(
    &format!("qrstatic:temporal:v1:spatial:{master_key}:frame:{frame_index}")
);
for idx in (1..len).rev() {
    let swap_idx = (rng.next_u64() as usize) % (idx + 1);
    permutation.swap(idx, swap_idx);
}
```

Not a block shuffle — every cell can map to any physical position. The QR is never laid out in a stable centered position in physical space. The decoder inverts this with `unpermute_grid` before correlating.

### Encoding — frame generation

Each frame starts from noise (or zeros for signal-only mode). For each logical cell index, compute the physical index via the per-frame permutation, then add:

```
frame[physical] += l1_amplitude * signal_map[logical] * chip[frame][logical]
```

The signal map maps QR modules to `+1/-1` (white = +1, black = -1), centered in the larger frame shape.

### Decoding — keyed matched-filter correlation

```rust
for frame_index in 0..frames.len() {
    let permutation = frame_permutation(temporal_key, frame_index, ...);
    let logical_frame = unpermute_grid(&frames[frame_index], &permutation);
    for ((acc, &sample), &chip) in data.iter_mut()
        .zip(logical_frame.data().iter())
        .zip(schedule[frame_index].data().iter())
    {
        *acc += sample * chip;
    }
}
```

Chips that matched the encoding amplify the signal. Chips that opposed it cancel noise. The correlation field reveals the QR.

### Detector score — explicit threshold gating

```rust
pub fn detector_score(field: &Grid<f32>) -> f32 {
    field.data().iter().map(|v| v.abs()).sum::<f32>() / field.len() as f32
}
```

Mean of absolute values. If the score is below `TemporalDecodePolicy.min_detector_score`, the decode is rejected before any QR extraction is attempted. Wrong keys produce near-zero-mean correlation fields, so the score stays low and the codec returns a `Codec` error — no garbage output.

### Progressive decode

`correlate_prefix` accepts fewer than `n_frames` frames. This powers the prefix-acquisition sweeps in the eval harness. The codec can tell you how confident it is at any point in the window.

### Layer 2 — under the temporal carrier

Layer 2 packetizes a payload into bits, maps to `±1`, tiles across frame cells. Encoded simultaneously:

```rust
let l1 = config.l1_amplitude * signal_map[logical] * l1_schedule[frame][logical];
let l2 = layer2.amplitude * l2_signal_map[logical] * l2_schedule[frame][logical];
frame[physical] += l1 + l2;
```

Layer 2 recovery requires Layer 1 first. The decoder reconstructs the expected L1 contribution and subtracts it:

```rust
let l1 = config.l1_amplitude * l1_signal_map[logical] * l1_schedule[frame][logical];
let residual = logical_frame[logical] - l1;
*acc += residual * l2_schedule[frame][logical];
```

### Key derivation — domain-separated, versioned

All temporal randomness driven by Xoshiro256** seeded via SHA-256 of domain-separated strings:

| Domain | Seed format |
|---|---|
| L1 chips | `qrstatic:temporal:v1:l1:{master_key}:cell:{cell_idx}` |
| L2 chips | `qrstatic:temporal:v1:l2:{master_key}:cell:{cell_idx}` |
| Spatial permutation | `qrstatic:temporal:v1:spatial:{master_key}:frame:{frame_index}` |
| Noise | `qrstatic:temporal:v1:noise:{master_key}:frame:{frame_index}` |
| Tile scatter | `qrstatic:temporal:v1:tiled:scatter:{master_key}` |

The `v1` tag enables future version migration without ambiguity.

### Spec vs implementation

The design document (`TEMPORAL.md`) is honest about what's implemented vs aspirational:

**Implemented and matching spec:** Analog `Grid<f32>` carrier, balanced chip schedules, per-frame spatial permutation, keyed matched filtering, detector score, threshold gating, Layer 2 subtraction, Reed-Solomon packet FEC, tiled scatter assignment, carrier overlay.

**Not yet implemented (spec admits this):** Layer 1 bootstrap of Layer 2 profile (supplied out-of-band), blind synchronization, Walsh/Hadamard or Gold code families, framed mode (partial recovery), payload whitening/encryption, real video compression survival.

**One stale spec claim:** TEMPORAL.md says "payload efficiency is poor because shard bytes are hex-encoded into QR text." The code now uses raw byte mode QR encoding, so this is no longer true. The refactor improved payload density substantially.

## Stage 2 Packet Layer — Source Analysis

### Packet framing

`TemporalPacket` has a 20-byte fixed header: version (1), flags (1), block_id (4), packet_id (2), data_shards (1), parity_shards (1), payload_bytes_per_packet (2), block_payload_len (4), payload_crc32 (4). Variable payload follows.

### CRC32

Standard CRC-32 with polynomial `0xEDB88320` (reflected), init `0xFFFFFFFF`, final XOR `0xFFFFFFFF`. Every packet's payload is CRC-protected.

### Reed-Solomon erasure recovery

The systematic generator matrix is a Vandermonde matrix over GF(256) with evaluation points `x = 1, 2, ..., total_shards`, multiplied by the inverse of the top `data_shards × data_shards` block to produce a systematic generator (first rows form identity).

Erasure recovery collects unique packet IDs, requires at least `data_shards` survivors, builds a decode matrix from the generator rows of the received shards, inverts it via Gauss-Jordan over GF(256), and multiplies to recover original data. Standard erasure-only RS decoding — no error correction, only erasure filling.

## Tiled Transport — Source Analysis

### Tile arrangement

The video frame is divided into QR-sized tiles. `tiles_x = video_width / tile_size`, `tiles_y = video_height / tile_size`. Remainder pixels become inactive border. Only `active_tiles = n_groups * group_size` tiles carry data.

### Keyed tile assignment

A keyed Fisher-Yates shuffle of all tile indices, then round-robin assignment to `(group_id, shard_index)`. Group 0 is the control group (carries session metadata). Groups 1+ are payload groups. Adjacent tiles never belong to the same group.

### Per-tile key derivation

```rust
fn derive_tile_key(master_key: &str, tile_index: usize) -> String {
    format!("{}:tile:{}", master_key, tile_index)
}
```

Each tile gets a fully independent temporal codec instance with its own chip schedule, spatial permutation, and noise stream.

### Carrier overlay

Each tile's signal-only temporal stream is added to the corresponding region of supplied carrier frames, then clamped:

```rust
let value = frame[(oy+row, ox+col)] + tile_frame[(row, col)];
frame[(oy+row, ox+col)] = value.clamp(-clip_limit, clip_limit);
```

The codec sits above raw frame access and below the final video encoder. It does not handle container, muxing, timestamp, or transport responsibilities.

## Eval Harnesses — Source Analysis

### Stage 1 eval (`temporal_eval.rs`)

Each trial runs four decode scenarios:

| Scenario | Construction |
|---|---|
| Correct decode | Encode with `master_key`, decode with same key |
| Wrong key | Encode with `master_key`, decode with different key string |
| Wrong window | Drop `frames[0]`, append frame 0 from a different encoding session |
| Naive accumulation | Sum all frames without key correlation, attempt QR extraction |

The wrong-window test is particularly well-constructed: it simulates a boundary error where the receiver's window is off by one frame and overlaps with an unrelated stream.

The prefix sweep takes `frames[..prefix_len]` for each prefix length, calls `correlate_prefix`, records detector score and decode success. `k50` is the smallest prefix where ≥50% of trials decode. `k95` is the smallest prefix where ≥95% decode.

### Stage 1 results

The `middle-64-a` profile (41×41, 64 frames, noise=0.42, l1=0.22, threshold=6.0):

| Metric | Value |
|---|---|
| Full-window correct decode | 100% |
| Wrong-key decode | 0% |
| Wrong-window decode | 0% |
| Naive decode | 0% |
| Correct decode through 44/64 frames | 0% |
| Correct decode at 48/64 frames | 12.5% |
| Correct decode at 52/64 frames | 100% |
| k50 | 52 |
| k95 | 52 |

Detector score separation:

| Path | Mean score |
|---|---|
| Correct key | 7.819 |
| Wrong key | 1.845 |
| Wrong window | 1.843 |
| Naive | 1.841 |

Margin: 5.973 between correct and wrong-key. Clean separation.

Earlier profiles (`baseline-64/96/128`) were rejected as defaults despite perfect decode rates — they were too strong, meaning the signal revealed too aggressively. The eval philosophy: profiles that decode perfectly but are too visually aggressive are not accepted as defaults.

### Tiled eval (`temporal_tiled_eval.rs`)

Measures capacity vs reliability across frame geometry and QR version. When carrier profiles are enabled (flat/gradient/motion), measures visual artifacts:

```
mean_abs_delta = mean(|encoded - carrier|)
max_abs_delta = max(|encoded - carrier|)
psnr_db = 20*log10(2*clip_limit) - 10*log10(mse)
```

Quantization drift: encoded frames quantized to N levels, then delta measured against pre-quantized frames.

### Tiled results

Throughput profile (`tiled-v4-balanced`, 660×495, v4, l1=0.09):

| Metric | Value |
|---|---|
| Active tiles | 300 |
| Max payload | 5,660 bytes |
| Carrier PSNR | 26.29 dB |
| Block success (q128) | 8/8 |
| Block success (q16) | 4/4 |
| Block success (q8) | 4/4 (299.75/300 tiles) |
| Block success (q4) | 0/4 (destructive) |

The original `l1=0.22` setting was too aggressive for carrier overlay: PSNR of 18.59 dB. The amplitude sweep found 0.07 (v3) and 0.09 (v4) as the gentlest plausible operating points.

The eval document is honest about limitations: quantization is only a crude proxy for real video compression. H.264/HEVC/AV1 behavior is not yet tested.

## Test Suite — Source Analysis

**226 total tests** (150 inline unit + 68 integration + 8 CLI/container).

### Temporal tests (the security-critical ones)

The 7 temporal integration tests prove the steganographic security properties:

1. Correct key recovers QR payload (score > 1.0)
2. Wrong key fails closed (decode error)
3. Wrong window fails closed (decode error)
4. Naive accumulation does not decode (the core steganographic property)
5. Correct-key score exceeds wrong-key and naive baselines (quantitative separation)
6. Single frame does not reveal centered QR layout (<70% agreement with QR grid)
7. Layer 2 packet payload roundtrip works alongside Layer 1 QR

### Packet tests

3 tests: binary roundtrip with CRC mismatch detection, multi-block erasure recovery (2 packets erased, still recovers), and insufficient-shards failure.

### Experimental codec tests

Each codec has 5–9 integration tests covering: roundtrip, determinism, streaming equivalence, partial-frame failure, random-frame failure, dimension mismatch, minimum-frame-count rejection, payload capacity. Test honesty: `test_biased_insufficient_frames_mismatches` explicitly verifies that insufficient frames produce the *wrong* answer, not an error.

### Companion test file pattern

Each codec has a companion helper in `tests/common/` providing roundtrip functions. Integration test files include helpers via `#[path = "common/xor.rs"] mod xor_common;`. This keeps test helpers DRY without a separate test-support crate.

## Debug Viewers

### macOS viewer (`qrstatic-debug-macos`)

`eframe`/`egui` native desktop app. 938 lines. Shows live frame, naive accumulator, correlation field, detector score, L1 decode track (window thumbnails), and L2 data track (signed accumulation bar chart). Real-time computation per frame tick.

### TUI viewer (`qrstatic-debug-tui`)

`ratatui`/`crossterm`. 4 files, ~960 lines. Half-block rendering (`▀`) for grid display — each terminal row renders two grid rows. Shows raw stream, correlation field, QR decode panel, L1 track, and L2 hex dump. Keyboard controls: Space (play/pause), n/Right (step), q (quit).

## Adversarial Skill

The repo includes `skills/noise-channel-analysis/` — a red-team skill for breaking steganographic channels like qrstatic. It describes how an attacker would approach the same channels the eval harnesses prove are secure:

- Characterize cover signal → hunt for leakage → apply transforms → search for synchronization → exploit redundancy → review code
- Transform arsenal: histograms, differencing, accumulation (XOR/sum/majority), threshold, geometry recovery, oracle (format parsing, QR finder scoring)
- Specific attack notes for QR-in-noise designs: test accumulation over window sizes, search for finder patterns, score grids with QR format consistency, use QR decode as oracle

The skill is the adversarial counterpart to the eval harnesses. Its existence signals that the author treats security claims as falsifiable, not asserted.

## Presentation Narrative

The `prompts/` directory contains 10 slide prompts documenting the codec evolution as a presentation. The narrative is explicitly evolutionary: each codec learns from the previous one's failure.

| Slide | Codec | Limitation bridging to next |
|---|---|---|
| 1 | XOR | No payload, no magnitude, no graceful degradation |
| 2 | Signed | Still binary, no payload |
| 3 | Binary | No noise model |
| 4 | Analog | Single channel only |
| 5 | Layered | Fixed window boundaries |
| 6 | Sliding | Still spatially detectable |
| 7 | Audio | Carrier-specific |
| 8 | **Temporal** | Addresses all prior weaknesses |
| 8b | Research basis | DSSS + watermarking + Reed-Solomon |

Slide 8 declares temporal as "the codec that learned from all the others." Slide 8b grounds the design in established theory, citing Stojanovic (DSSS acquisition), Cox (spread-spectrum watermarking), and Geisel/JPL (Reed-Solomon).

## CLI

Only the `binary` codec is exposed through the CLI (`encode binary` / `decode binary`). Other codecs are library-only.

The `.qrsb` container format: 4-byte magic (`QRSB`), version, flags (packed/unpacked), dimensions, frame count, payload length, bias parameters, seed, then frame data. Frame cells are `i8` values (-1/+1). Packed mode stores one bit per cell (LSB-first).

The `--optimize` flag searches for the smallest viable configuration by iterating dimensions and frame counts, performing full encode→decode roundtrips until one succeeds.

## Patterns

Several recur across the QR static family and the author's other work:

- **Clean break over deprecation.** The temporal codec did not deprecate the experimental codecs. It was built alongside them, the docs were rewritten to center it, and the experiments were archived with a clear "these are not production" header.

- **Prior art before invention.** The temporal codec cites three papers and explains the specific practical takeaway from each. The design correction (signal in temporal correlation, not per-frame mean) is framed as a consequence of DSSS theory, not a novel insight.

- **Zero dependencies as discipline.** Both Rust repos hand-roll SHA-256, GF(2⁸), Reed-Solomon, and QR encode/decode with no external crates. This is a hard constraint. The Python prototype's dependency on NumPy/OpenCV/`qrcode` is the contrast that motivates the constraint.

- **Evals drive defaults.** The Stage 1 default was chosen not from the strongest profile but from the first one that landed in the intended concealment band. Profiles that were "too strong" were rejected despite perfect decode rates.

- **Structural guarantees over probabilistic ones.** The chip balance is enforced by construction (exact N/2 of each sign, Fisher-Yates shuffled), not by statistical expectation. The spatial permutation is a total bijection, not a soft scramble. The hygiene ratchet is a compile-time test, not a code review guideline.

- **Honest about gaps.** The spec documents what's not implemented. The eval document states what's not proven. The README notes that the QR decoder only handles its own output. No claim is made stronger than the evidence supports.

- **Burst development.** Python prototype: one day. Production Rust: two days. Riptide: one day. The work happens in concentrated sessions with long gaps between.

- **Carrier overlay, not carrier replacement.** The temporal codec adds a weak keyed signal onto existing video frames before compression, then recovers it from decoded frames. It does not want to be a video codec.

## What the Python Prototype Got Wrong

Source analysis reveals specific issues the Rust rewrite addressed:

1. **No tests.** Zero `test_*.py` files. The Rust repos have 226 tests with hygiene enforcement.
2. **RNG coupling fragility.** Analog/layered/signed/sliding all regenerate noise from the QR seed and subtract it. This couples encode/decode RNG consumption order tightly. The signed codec has an off-by-one RNG desynchronization bug. The temporal codec eliminates this by using keyed correlation instead of noise subtraction.
3. **Library dependency.** QR generation and detection delegated to `qrcode` and OpenCV. The Rust repos hand-roll the entire QR stack.
4. **Signal in the per-frame mean.** Every codec embeds the QR signal in a dimension accessible to naive accumulation. The temporal codec moves it into keyed temporal correlation.
5. **Inconsistent APIs.** Binary streaming encoder ignores payload. Sliding streaming decoder lacks L2. Layered streaming encoder pre-materializes all frames.
6. **Duplicated code with divergence.** Six files copy-paste the same helpers with subtle differences (threshold operators, padding strategies).

## File Inventory

### Production (`qrstatic/`)

```
crates/
  qrstatic/                 Core library (zero dependencies, 150 unit tests)
    src/
      lib.rs, error.rs, grid.rs, sha256.rs, prng.rs, bits.rs
      qr/                   encode, decode, gf256, reed_solomon, mask, format
      codec/
        temporal.rs         Production Layer 1 codec
        temporal_packet.rs  Stage 2 packet/FEC layer
        temporal_tiled.rs   Tiled transport variant
        xor.rs, signed.rs, binary.rs, analog.rs, layered.rs, sliding.rs, audio.rs
        common.rs           Shared utilities (pub(crate))
        mod.rs              Module integration
    tests/                  68 integration tests + common/ helpers + hygiene.rs
  qrstatic-cli/             Binary payload CLI + temporal eval + tiled eval
  qrstatic-debug-macos/     egui native viewer (938 lines)
  qrstatic-debug-tui/       ratatui terminal viewer (4 files, ~960 lines)
TEMPORAL.md                 Production codec design document (900 lines)
CODECS.md                   Experimental codec documentation (730 lines)
EVALS.md                    Eval harness documentation (430 lines)
PLAN.md                     Historical build plan
temporal_results.tsv        Stage 1 raw eval data
temporal_tiled_results.tsv  Tiled transport raw eval data
prompts/                    10 presentation slide prompts
skills/noise-channel-analysis/  Adversarial analysis skill
```

### Riptide (`qrstatic-riptide/`)

```
src/
  lib.rs, main.rs, frame.rs
  qr/         galois, version, reed_solomon, encode, matrix, decode
  crypto/     sha256, prng
  codec/      xor, accumulator, biased, windowed, multilayer, audio
```

### Python prototype (`qr-static-stream/`)

```
qr_static.py          XOR (7,269 bytes)
qr_static_analog.py   Analog grayscale (13,839 bytes)
qr_static_binary.py   Binary static (9,392 bytes)
qr_static_layered.py  Two-layer recursive (15,848 bytes)
qr_static_sliding.py  Sliding window (17,502 bytes)
qr_static_signed.py   Signed accumulation (11,926 bytes)
qr_static_audio.py    Audio sign-flipping (10,070 bytes)
demo_*.py             One demo per codec
README.md             610 lines
requirements.txt      numpy, qrcode, opencv-python, pillow
```

## Source Material

- Full source analysis of all `.py` files in `qr-static-stream/` (7 codecs + 7 demos)
- Full source analysis of all `.rs` files in `qrstatic-riptide/` (16 files)
- Full source analysis of production repo primitives, QR stack, experimental codecs, temporal family, eval harnesses, CLI, debug viewers, and test suite
- `TEMPORAL.md`, `CODECS.md`, `EVALS.md`, `PLAN.md`
- `temporal_results.tsv`, `temporal_tiled_results.tsv`
- Git logs for all three repositories
