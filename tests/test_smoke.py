from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]


class StaticExperienceTests(unittest.TestCase):
    def test_entrypoints_are_real_interactive_documents(self):
        for relative in ("index.html", "site/index.html"):
            html = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("<main>", html)
            self.assertIn('id="sessions"', html)
            self.assertIn('data-session="judas"', html)
            self.assertIn("prefers-reduced-motion", html)
            self.assertNotIn("Sitio en construcción", html)
            self.assertNotIn("Motor 3D &amp; Códice</p>", html)

    def test_vercel_config_does_not_require_a_missing_build_package(self):
        config = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
        self.assertEqual(config["version"], 2)
        self.assertNotIn("builds", config)
        self.assertTrue(config["cleanUrls"])


if __name__ == "__main__":
    unittest.main()
