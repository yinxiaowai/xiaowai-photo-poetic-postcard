# Changelog

## 1.1.0 - 2026-09-05

- Added a mandatory downstream prompt compiler directly to `SKILL.md` so intermediary Agents cannot replace the full contract with a one-paragraph summary.
- Added five fixed prompt sections, concrete subject and omission-list resolution, placeholder checks, and a pre-generation gate.
- Changed the default panel split to a strict 50/50 for higher reliability across weaker image Agents.
- Defined each of the three swatches as a perfect flat-color square with a side length near 1/20 of lower-panel width.
- Hardened the standalone Chinese and English Prompt MD files against prompt summarization, whole-scene repainting, and automatic multi-style requests.
- Added cross-Agent troubleshooting notes to both READMEs and installation guides.

## 1.0.1 - 2026-09-04

- Replaced the flower-arch gallery case with a new Golden Hall source and verified 3:4 one-shot result.
- Recorded the visible `金殿` plaque as subject-name evidence without inventing a broader location.
- Made WorkBuddy package metadata read its version from the repository `VERSION` file.

## 1.0.0 - 2026-09-03

- Rebuilt the private Codex workflow as a model-neutral Agent Skill.
- Changed delivery from four candidates to one final image.
- Added honest vision/generation fallback behavior.
- Added standalone Chinese and English Prompt MD files.
- Added Codex, Claude Code, Gemini CLI, WorkBuddy, Dreamina, and Doubao guidance.
- Added user-adjustable dimensions, panel split, style, layout, typography, paper, swatches, and color controls.
- Enforced one-shot integrated generation for the complete postcard, including typography, swatches, and layout; separate panel generation, stitching, and programmatic text overlays are prohibited.
- Replaced fragile photo margins and hairlines with a full-width, borderless upper photo and cover-style cropping; reduced default lower-subject scale for weaker image models.
- Hardened subject extraction around deconstruct/selective-preservation/distill/reconstruct, requiring the recognizable environment to be omitted.
- Added adaptive subject/text/swatch placement, a minimum visible whitespace target, and actual pixel-ratio verification so 2:3 outputs cannot pass as 3:4.
- Added a place-evidence hierarchy and made confirmed place or landmark names mandatory in the title or note, while prohibiting guesses when evidence is insufficient.
- Added standard and WorkBuddy package builders plus repository validation.
- Added bilingual documentation and layered content/code/asset licensing.
