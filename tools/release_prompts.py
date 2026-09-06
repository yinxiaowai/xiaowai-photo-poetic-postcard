#!/usr/bin/env python3
"""Check versioned MD entry points and export exact tagged prompts for Releases."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard"
PROMPTS = tuple(f"photo-poetic-postcard-prompt.{lang}.md" for lang in ("zh-CN", "en"))
ENTRY_DOCUMENTS = ("README.md", "README_EN.md", "docs/INSTALLATION.md", "docs/INSTALLATION_EN.md")


def check_entries(root: Path = ROOT) -> list[str]:
    tag = "v" + (root / "VERSION").read_text(encoding="utf-8").strip()
    errors = []
    pattern = re.compile(re.escape(REPO_URL) + r"/blob/([^/]+)/references/photo-poetic-postcard-prompt\.[\w-]+\.md")
    for relative in ENTRY_DOCUMENTS:
        text = (root / relative).read_text(encoding="utf-8")
        versions = pattern.findall(text)
        if not versions or any(value != tag for value in versions):
            errors.append(f"{relative}: online prompt links must pin VERSION ({tag}), found {versions}")
        if re.search(r"\]\((?:\.\./)?references/photo-poetic-postcard-prompt\.", text):
            errors.append(f"{relative}: public entry must not use a relative/development prompt link")
        for name in PROMPTS if relative.startswith("README") else ():
            for url in (f"{REPO_URL}/blob/{tag}/references/{name}", f"{REPO_URL}/releases/latest/download/{name}"):
                if url not in text:
                    errors.append(f"{relative}: missing entry {url}")
    return errors


def git_bytes(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), *args], check=True, stdout=subprocess.PIPE).stdout


def export_tag(tag: str, output_dir: Path, root: Path = ROOT) -> dict:
    if not re.fullmatch(r"v\d+\.\d+\.\d+", tag):
        raise ValueError("A stable vMAJOR.MINOR.PATCH tag is required")
    ref = f"refs/tags/{tag}"
    commit = git_bytes(root, "rev-parse", "--verify", f"{ref}^{{commit}}").decode().strip()
    version = git_bytes(root, "show", f"{ref}:VERSION").decode().strip()
    if tag != f"v{version}":
        raise ValueError(f"Tag {tag} disagrees with its VERSION {version}")
    payloads = {name: git_bytes(root, "show", f"{ref}:references/{name}") for name in PROMPTS}
    manifest = {
        "tag": tag,
        "commit": commit,
        "files": {name: {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)} for name, data in payloads.items()},
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, data in payloads.items():
        (output_dir / name).write_bytes(data)
    (output_dir / "prompt-release.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", help="Export MD assets from this existing stable tag, never from the worktree")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist" / "prompts")
    args = parser.parse_args()
    errors = check_entries()
    if errors:
        print("\n".join(errors))
        return 1
    print("Prompt version entry checks passed.")
    if args.tag:
        print(json.dumps(export_tag(args.tag, args.output_dir), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
