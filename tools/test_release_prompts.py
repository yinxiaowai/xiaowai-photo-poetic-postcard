"""Regression checks for public version links and immutable prompt exports."""

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import release_prompts as release


class ReleasePromptTests(unittest.TestCase):
    def entries(self, root):
        (root / "VERSION").write_text("1.3.0\n", encoding="utf-8")
        text = "\n".join(
            f"{release.REPO_URL}/{suffix}"
            for name in release.PROMPTS
            for suffix in (f"blob/v1.3.0/references/{name}", f"releases/latest/download/{name}")
        )
        for name in release.ENTRY_DOCUMENTS:
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def test_current_entries_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.entries(root)
            self.assertEqual(release.check_entries(root), [])

    def test_version_bump_requires_entry_updates(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.entries(root)
            (root / "VERSION").write_text("1.4.0\n", encoding="utf-8")
            self.assertTrue(release.check_entries(root))

    def test_main_and_relative_entries_fail(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.entries(root)
            path = root / "README.md"
            text = path.read_text(encoding="utf-8").replace("/blob/v1.3.0/", "/blob/main/")
            path.write_text(text + "\n[MD](references/photo-poetic-postcard-prompt.en.md)", encoding="utf-8")
            errors = release.check_entries(root)
            self.assertTrue(any("main" in error for error in errors))
            self.assertTrue(any("relative" in error for error in errors))

    def test_export_uses_tagged_bytes_and_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            payload = "# 完整绘图规范\n\nTagged content.\n".encode()
            def fake_git(_root, *args):
                self.assertIn("refs/tags/v1.3.0", " ".join(args))
                if args[0] == "rev-parse":
                    return b"a" * 40 + b"\n"
                return b"1.3.0\n" if args[-1].endswith(":VERSION") else payload
            with patch.object(release, "git_bytes", side_effect=fake_git):
                manifest = release.export_tag("v1.3.0", root / "out", root)
            self.assertEqual(manifest["tag"], "v1.3.0")
            for name in release.PROMPTS:
                self.assertEqual((root / "out" / name).read_bytes(), payload)
                self.assertEqual(manifest["files"][name]["sha256"], hashlib.sha256(payload).hexdigest())
            self.assertEqual(json.loads((root / "out/prompt-release.json").read_text()), manifest)

    def test_tag_version_mismatch_fails_before_writing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with patch.object(release, "git_bytes", side_effect=[b"a" * 40, b"1.2.0\n"]):
                with self.assertRaises(ValueError):
                    release.export_tag("v1.3.0", root / "out", root)
            self.assertFalse((root / "out").exists())

    def test_invalid_tag_fails_before_git(self):
        with patch.object(release, "git_bytes") as git:
            with self.assertRaises(ValueError):
                release.export_tag("main", Path("unused"))
            git.assert_not_called()


if __name__ == "__main__":
    unittest.main()
