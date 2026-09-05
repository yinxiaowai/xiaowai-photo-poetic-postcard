#!/usr/bin/env python3
"""Run lightweight structural and policy checks for this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "README_EN.md",
    "SKILL.md",
    "agents/openai.yaml",
    "references/postcard-design.md",
    "references/photo-poetic-postcard-prompt.zh-CN.md",
    "references/photo-poetic-postcard-prompt.en.md",
    "LICENSE",
    "LICENSE-CODE",
    "NOTICE.md",
)
FORBIDDEN_IN_SKILL = (
    "only uses codex",
    "本 skill 只使用 codex",
    "about 48%",
    "about 52%",
    "约 48%",
    "约 52%",
)
REQUIRED_IN_SKILL = (
    "one image-generation operation",
    "downstream prompt compiler",
    "mandatory downstream prompt contract",
    "downstream prompt preflight",
    "不得概括",
    "【画面结构】",
    "【上半区｜原摄影锁定】",
    "【下半区｜单一主体转绘】",
    "【文字与三枚色卡】",
    "【禁止项与交付】",
    "上下两个独立区域",
    "上下等高、各占50%",
    "只提取并转绘",
    "1/20",
    "100%均匀纯色平涂",
    "do not generate the lower panel separately",
    "do not use a local compositor",
    "do not overlay title",
    "fills the upper region edge to edge",
    "no paper gap, hairline",
    "at least about 45%",
    "deconstruct → selective preservation → distill → reconstruct",
    "do not default every result to lower-right",
    "a 2:3 result fails",
    "exact place or landmark name must appear verbatim",
    "if the host automatically returns multiple images",
)
REMOVED_IMPLEMENTATION_PATHS = (
    "scripts/compose_postcard.py",
    "scripts/requirements.txt",
    "tests/test_compose_postcard.py",
)
OBSOLETE_WORKFLOW_TEXT = (
    "python scripts/compose_postcard.py",
    "## 可选：保证上方照片忠实的本地合成",
    "## optional exact-photo compositor",
    "skill 会优先采用“下半区生图 + 本地确定性合成”",
)
REQUIRED_GALLERY = (
    "examples/gallery/sources/case-01-xiaoqikong-source.webp",
    "examples/gallery/sources/case-02-shaolin-source.webp",
    "examples/gallery/sources/case-03-kitten-source.webp",
    "examples/gallery/sources/case-04-golden-hall-source.webp",
    "examples/gallery/sources/case-05-portrait-source.webp",
    "examples/gallery/sources/case-06-riverside-source.webp",
    "examples/gallery/results/case-01-xiaoqikong-result.webp",
    "examples/gallery/results/case-02-shaolin-result.webp",
    "examples/gallery/results/case-03-kitten-result.webp",
    "examples/gallery/results/case-04-golden-hall-result.webp",
    "examples/gallery/results/case-05-portrait-result.webp",
    "examples/gallery/results/case-06-riverside-result.webp",
)


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def webp_dimensions(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()
    if len(data) < 30 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return None
    position = 12
    while position + 8 <= len(data):
        kind = data[position : position + 4]
        size = int.from_bytes(data[position + 4 : position + 8], "little")
        chunk = data[position + 8 : position + 8 + size]
        if kind == b"VP8X" and len(chunk) >= 10:
            return 1 + int.from_bytes(chunk[4:7], "little"), 1 + int.from_bytes(chunk[7:10], "little")
        if kind == b"VP8L" and len(chunk) >= 5 and chunk[0] == 0x2F:
            bits = int.from_bytes(chunk[1:5], "little")
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
        if kind == b"VP8 " and len(chunk) >= 10 and chunk[3:6] == b"\x9d\x01\x2a":
            return int.from_bytes(chunk[6:8], "little") & 0x3FFF, int.from_bytes(chunk[8:10], "little") & 0x3FFF
        position += 8 + size + (size & 1)
    return None


def main() -> int:
    failures: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}", failures)

    for relative in REMOVED_IMPLEMENTATION_PATHS:
        if (ROOT / relative).exists():
            fail(f"obsolete compositing implementation still exists: {relative}", failures)

    for relative in REQUIRED_GALLERY:
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing required gallery file: {relative}", failures)
        elif "/results/" in relative:
            dimensions = webp_dimensions(path)
            if dimensions is None:
                fail(f"gallery result is not a valid WebP: {relative}", failures)
            elif dimensions[0] * 4 != dimensions[1] * 3:
                fail(f"gallery result is not exact 3:4: {relative} is {dimensions[0]}x{dimensions[1]}", failures)

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        if not skill.startswith("---\n") or "\n---\n" not in skill[4:]:
            fail("SKILL.md frontmatter is malformed", failures)
        name_match = re.search(r"(?m)^name:\s*([^\n]+)$", skill)
        if not name_match or name_match.group(1).strip() != "xiaowai-photo-poetic-postcard":
            fail("SKILL.md name is incorrect", failures)
        description_match = re.search(r"(?m)^description:\s*(.+)$", skill)
        if not description_match or len(description_match.group(1).strip()) < 40:
            fail("SKILL.md description is missing or too vague", failures)
        if len(skill.splitlines()) > 500:
            fail("SKILL.md exceeds 500 lines", failures)
        lowered = skill.lower()
        for phrase in FORBIDDEN_IN_SKILL:
            if phrase in lowered:
                fail(f"obsolete policy remains in SKILL.md: {phrase}", failures)
        for phrase in REQUIRED_IN_SKILL:
            if phrase not in lowered:
                fail(f"one-shot generation invariant missing from SKILL.md: {phrase}", failures)

    for relative in ("README.md", "README_EN.md"):
        path = ROOT / relative
        if not path.is_file():
            continue
        lowered = path.read_text(encoding="utf-8").lower()
        for phrase in OBSOLETE_WORKFLOW_TEXT:
            if phrase in lowered:
                fail(f"obsolete compositing workflow remains in {relative}: {phrase}", failures)

    link_pattern = re.compile(r"!?\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
    html_link_pattern = re.compile(r"(?:src|href)=\"(?!https?://|mailto:|#)([^\"]+)\"")
    for relative in ("README.md", "README_EN.md", "SKILL.md"):
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).resolve().exists():
                fail(f"broken local link in {relative}: {target}", failures)
        for target in html_link_pattern.findall(text):
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).resolve().exists():
                fail(f"broken local HTML link in {relative}: {target}", failures)

    prompt_contracts = {
        "references/photo-poetic-postcard-prompt.zh-CN.md": (
            "不得概括",
            "【画面结构】",
            "【上半区｜原摄影锁定】",
            "【下半区｜单一主体转绘】",
            "【文字与三枚色卡】",
            "【禁止项与交付】",
            "上下两个等高、独立的区域",
            "只提取并转绘",
            "具体删除清单",
            "无纸边、白边、描边",
            "纸张肌理和文艺留白只属于下半区",
            "1/20",
            "100% 均匀纯色平涂",
        ),
        "references/photo-poetic-postcard-prompt.en.md": (
            "without summarizing",
            "[canvas structure]",
            "[upper panel — source photo lock]",
            "[lower panel — one extracted subject]",
            "[typography and swatches]",
            "[prohibitions and delivery]",
            "50% each",
            "concrete omission list",
            "no paper margin, white bars, outline",
            "paper texture and artistic whitespace belong only to the lower panel",
            "1/20",
            "100% uniform and flat",
        ),
    }
    for relative, required_phrases in prompt_contracts.items():
        path = ROOT / relative
        if path.is_file():
            text = path.read_text(encoding="utf-8").lower()
            for token in ("one", "一张"):
                if token in text:
                    break
            else:
                fail(f"standalone prompt does not enforce one output: {relative}", failures)
            for phrase in required_phrases:
                if phrase.lower() not in text:
                    fail(f"standalone prompt contract missing in {relative}: {phrase}", failures)
            for phrase in ("about 48%", "about 52%", "约 48%", "约 52%"):
                if phrase in text:
                    fail(f"obsolete flexible default remains in {relative}: {phrase}", failures)

    if failures:
        print("Validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
