# Installation and Compatibility

## Two separate capability layers

1. **Skill layer:** can the host discover and read `SKILL.md`?
2. **Image layer:** does the current session have vision, reference-image generation/editing, and file-output capabilities?

Installing a Skill does not automatically add an image model. A vision-capable host without generation can still produce one fully resolved prompt for handoff.

## Standard Agent Skills package

### Codex

Codex currently reads user Skills from `$HOME/.agents/skills` and repository Skills from `.agents/skills`. Ask `$skill-installer` to install the GitHub repository, or clone it manually:

```bash
git clone https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git ~/.agents/skills/xiaowai-photo-poetic-postcard
```

Official documentation: [OpenAI — Build skills](https://developers.openai.com/codex/skills/)

### Claude Code

Personal Skills live at `~/.claude/skills/<skill-name>/SKILL.md`; project Skills live at `.claude/skills/<skill-name>/SKILL.md`.

```bash
git clone https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git ~/.claude/skills/xiaowai-photo-poetic-postcard
```

Official documentation: [Anthropic — Extend Claude with skills](https://code.claude.com/docs/en/skills)

Claude Code still needs a connected image model, MCP server, CLI, or other image tool to generate the final image. Otherwise the Skill returns a handoff prompt.

### Gemini CLI

```bash
gemini skills install https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git --consent
```

Official documentation: [Gemini CLI — Agent Skills](https://geminicli.com/docs/cli/skills/)

### Other hosts

Extract the standard release archive into the host's Skills directory while preserving `xiaowai-photo-poetic-postcard/SKILL.md`. See the [Agent Skills Specification](https://agentskills.io/specification).

## WorkBuddy package

WorkBuddy requires `skills/{skill-name}/SKILL.md` inside the ZIP plus platform-specific bilingual metadata, version, and author fields. Download `xiaowai-photo-poetic-postcard-workbuddy.zip` from Releases and upload it through WorkBuddy's Skill creation flow.

Official documentation: [WorkBuddy Open Platform — Skill](https://open.workbuddy.cn/en/docs/skill)

## Dreamina and Doubao

This project does not claim an unverified GitHub Skill installer for these products. Use the direct-prompt route:

1. Open an image-capable Agent or creation workspace.
2. Upload one source photo.
3. Paste the code block from the [Chinese](../references/photo-poetic-postcard-prompt.zh-CN.md) or [English](../references/photo-poetic-postcard-prompt.en.md) prompt.
4. Set any desired dimensions, split, medium, or copy.
5. Keep one final image; reject multi-image grids.

## Basic image tools

If the tool accepts a reference image but cannot analyze it conversationally, first ask a vision-capable Agent to identify the main element, supporting cues, three colors, title, and note. Fill those details into the prompt before generation.

If reference images are unsupported, the workflow cannot reliably preserve or derive from the source photo and should not be described as fully completed.

## Safety and privacy

- Review `SKILL.md` and its referenced files before installing any third-party Skill.
- Bundled Python tools only validate and package the repository; they do not generate, stitch, or typeset postcard artwork.
- Check the image platform's privacy terms before uploading sensitive or personal photos.
- Confirm copyright and model-release permissions before publishing examples.
