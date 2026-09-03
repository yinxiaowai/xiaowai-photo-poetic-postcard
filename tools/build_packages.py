#!/usr/bin/env python3
"""Build standard Agent Skills and WorkBuddy ZIP packages."""

from __future__ import annotations

import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "xiaowai-photo-poetic-postcard"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
STANDARD_ITEMS = (
    "SKILL.md",
    "agents",
    "references",
    "LICENSE",
    "LICENSE-CODE",
    "NOTICE.md",
    "VERSION",
)
WORKBUDDY_FRONTMATTER = f"""---
name: xiaowai-photo-poetic-postcard
display_name: 照片诗意明信片
display_name_en: Photo Poetic Postcard
description: 将一张照片制作成上方原摄影、下方单一主元素艺术转绘的一张诗意明信片；可在缺少生图能力时输出完整提示词。
description_zh: 一张原图生成一张可定制的照片与艺术转绘双画面明信片。
description_en: Turn one photo into one customizable poetic photo-and-illustration postcard.
version: {VERSION}
author: AI尹小歪
---
"""


def skill_body() -> str:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md has no YAML frontmatter")
    marker = text.find("\n---\n", 4)
    if marker < 0:
        raise ValueError("SKILL.md frontmatter is not closed")
    return text[marker + 5 :]


def copy_item(source: Path, destination: Path) -> None:
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def zip_tree(source: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source))


def build(output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    results: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="postcard-skill-") as temp_name:
        temp = Path(temp_name)

        standard_root = temp / "standard" / SKILL_NAME
        standard_root.mkdir(parents=True)
        for item in STANDARD_ITEMS:
            copy_item(ROOT / item, standard_root / item)
        standard_zip = output_dir / f"{SKILL_NAME}-standard.zip"
        zip_tree(temp / "standard", standard_zip)
        results.append(standard_zip)

        workbuddy_root = temp / "workbuddy" / "skills" / SKILL_NAME
        workbuddy_root.mkdir(parents=True)
        (workbuddy_root / "SKILL.md").write_text(
            WORKBUDDY_FRONTMATTER + skill_body(), encoding="utf-8", newline="\n"
        )
        for item in ("references", "LICENSE", "LICENSE-CODE", "NOTICE.md", "VERSION"):
            copy_item(ROOT / item, workbuddy_root / item)
        workbuddy_zip = output_dir / f"{SKILL_NAME}-workbuddy.zip"
        zip_tree(temp / "workbuddy", workbuddy_zip)
        results.append(workbuddy_zip)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    for path in build(args.output_dir.resolve()):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
