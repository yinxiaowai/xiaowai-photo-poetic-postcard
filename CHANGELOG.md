# Changelog

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
