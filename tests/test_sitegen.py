import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from sitegen import (  # noqa: E402
    BEGIN_MARKER,
    END_MARKER,
    render_projects,
    replace_generated_region,
    rank_repos,
    update_index,
)


class SitegenTests(unittest.TestCase):
    def test_ranking_preserves_tiers_and_skips_repositories(self):
        repos = [
            {
                "name": "zeta",
                "description": "zeta",
                "isPrivate": False,
                "defaultBranchRef": {"target": {"history": {"totalCount": 30}}},
            },
            {
                "name": "alpha",
                "description": "alpha",
                "isPrivate": False,
                "defaultBranchRef": {"target": {"history": {"totalCount": 30}}},
            },
            {
                "name": "personal",
                "description": "skip",
                "isPrivate": False,
                "defaultBranchRef": {"target": {"history": {"totalCount": 999}}},
            },
        ]

        rows, sections = rank_repos(repos)

        self.assertEqual([row["name"] for row in rows], ["alpha", "zeta"])
        self.assertEqual([row["name"] for row in sections["Featured Work"]], ["alpha", "zeta"])

    def test_rendering_escapes_public_data_and_never_links_private_repos(self):
        _, sections = rank_repos(
            [
                {
                    "name": "public&name",
                    "description": '<script>alert("x")</script>',
                    "isPrivate": False,
                    "defaultBranchRef": {"target": {"history": {"totalCount": 5}}},
                },
                {
                    "name": "secret",
                    "description": "internal details",
                    "isPrivate": True,
                    "defaultBranchRef": {"target": {"history": {"totalCount": 6}}},
                },
            ]
        )

        rendered = render_projects(sections)

        self.assertIn('href="https://github.com/ianzepp/public&amp;name"', rendered)
        self.assertIn("&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;", rendered)
        self.assertIn('secret <span class="badge-private">private</span>', rendered)
        self.assertNotIn("https://github.com/ianzepp/secret", rendered)

    def test_generated_region_is_idempotent_and_rejects_bad_seams(self):
        document = f"<header>stable</header>\n{BEGIN_MARKER}\nold\n{END_MARKER}\n<footer>stable</footer>\n"
        generated = "  <div>generated</div>"

        first = replace_generated_region(document, generated)
        second = replace_generated_region(first, generated)

        self.assertEqual(first, second)
        self.assertEqual(first.splitlines()[0], "<header>stable</header>")
        self.assertEqual(first.splitlines()[-1], "<footer>stable</footer>")
        self.assertIn(f"\n{END_MARKER}\n", first)

        with self.assertRaisesRegex(ValueError, "exactly one"):
            replace_generated_region(document.replace(BEGIN_MARKER, ""), generated)
        with self.assertRaisesRegex(ValueError, "alone"):
            replace_generated_region(document.replace(BEGIN_MARKER, f"<main>{BEGIN_MARKER}"), generated)

    def test_update_index_does_not_touch_sibling_assets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            index = root / "index.html"
            asset = root / "install.sh"
            index.write_text(f"before\n{BEGIN_MARKER}\nold\n{END_MARKER}\nafter\n", encoding="utf-8")
            asset.write_bytes(b"#!/bin/sh\necho stable\n")
            asset_before = asset.read_bytes()

            self.assertTrue(update_index(index, "new"))
            self.assertFalse(update_index(index, "new"))
            self.assertEqual(asset.read_bytes(), asset_before)


if __name__ == "__main__":
    unittest.main()
