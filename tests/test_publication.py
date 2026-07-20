import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SOURCE_FILES = {
    "CNAME",
    "README.md",
    "index.html",
    "llms.txt",
    "llms-full.txt",
    "ranking.sh",
    "robots.txt",
    "sitegen.py",
    "sitemap.xml",
}


class PublicationSafetyTests(unittest.TestCase):
    def served_files(self):
        excluded_directories = {".git", ".vivi", ".claude", "__pycache__"}
        return {
            path.relative_to(ROOT)
            for path in ROOT.rglob("*")
            if path.is_file()
            and not any(part in excluded_directories for part in path.relative_to(ROOT).parts)
        }

    def test_tracked_tree_excludes_private_sources_and_installers(self):
        served = self.served_files()

        self.assertNotIn(Path("content/CAREER-HISTORY.md"), served)
        self.assertFalse(
            any(path.as_posix().endswith("/install.sh") for path in served),
            "unsafe install scripts must not be in the publication tree",
        )

    def test_public_sources_have_no_local_absolute_paths(self):
        forbidden_fragments = (
            "/Users/",
            "/private/",
            "/Desktop/",
            "~/github/",
            "~/work/",
            "/tmp/",
        )

        for relative in sorted(PUBLIC_SOURCE_FILES):
            text = (ROOT / relative).read_text(encoding="utf-8")
            for fragment in forbidden_fragments:
                self.assertNotIn(
                    fragment,
                    text,
                    f"{relative} exposes local path fragment {fragment!r}",
                )

    def test_index_generated_region_is_public_and_well_formed(self):
        document = (ROOT / "index.html").read_text(encoding="utf-8")
        begin = "<!-- BEGIN GENERATED PROJECTS -->"
        end = "<!-- END GENERATED PROJECTS -->"
        self.assertEqual(document.count(begin), 1)
        self.assertEqual(document.count(end), 1)

        region = document.split(begin, 1)[1].split(end, 1)[0]
        self.assertNotIn('class="badge-private"', region)
        self.assertNotIn("/Users/", region)
        self.assertNotIn("/private/", region)

    def test_public_page_has_basic_semantic_and_accessible_structure(self):
        document = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('<html lang="en">', document)
        self.assertEqual(document.count("<h1>"), 1)
        self.assertIn('<nav class="nav shell" aria-label="Primary navigation">', document)
        self.assertIn('<main id="top">', document)
        self.assertIn("<footer>", document)
        self.assertIn('type="search"', document)
        self.assertIn('aria-label="Filter repositories"', document)
        self.assertIn("a:focus-visible", document)

    def test_public_page_has_no_third_party_font_fetches(self):
        document = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("fonts.googleapis.com", document)
        self.assertNotIn("fonts.gstatic.com", document)

    def test_real_page_generated_replacement_is_idempotent(self):
        from sitegen import replace_generated_region

        document = (ROOT / "index.html").read_text(encoding="utf-8")
        generated = "  <div class=\"project\">public-only</div>"
        first = replace_generated_region(document, generated)
        second = replace_generated_region(first, generated)
        self.assertEqual(first, second)
        self.assertEqual(first.count("<!-- BEGIN GENERATED PROJECTS -->"), 1)
        self.assertEqual(first.count("<!-- END GENERATED PROJECTS -->"), 1)

    def test_local_fragments_resolve(self):
        from html.parser import HTMLParser

        class AnchorParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.ids = set()
                self.fragments = []

            def handle_starttag(self, tag, attrs):
                values = dict(attrs)
                if "id" in values:
                    self.ids.add(values["id"])
                if tag == "a" and values.get("href", "").startswith("#"):
                    self.fragments.append(values["href"][1:])

        parser = AnchorParser()
        parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
        self.assertEqual(
            sorted(set(parser.fragments) - parser.ids),
            [],
            "every local anchor target must exist",
        )


if __name__ == "__main__":
    unittest.main()
