## About the author

Created by **AI Yin Xiaowai**, guest lecturer at the China Academy of Art AI Center, WaytoAGI-certified instructor, founder of Video Academy, AIGC practitioner, AI tool reviewer, and enterprise AI trainer.

Follow the official account for in-depth written guides, or the Channels account for hands-on demos and video tutorials.

<table>
  <tr>
    <td align="center" valign="top" width="50%">
      <strong>WeChat Official Account | Xiaowai's AI Toolbox</strong><br>
      AI news, step-by-step guides, and full written breakdowns<br><br>
      <a href="assets/images/wechat-qr.png"><img src="assets/images/wechat-qr.png" width="314" alt="Xiaowai's AI Toolbox WeChat QR code"></a>
    </td>
    <td align="center" valign="top" width="50%">
      <strong>WeChat Channels | AI Yin Xiaowai</strong><br>
      Tool tests, case demonstrations, and video tutorials<br><br>
      <a href="assets/images/wechat-channels-qr.jpg"><img src="assets/images/wechat-channels-qr.jpg" width="220" alt="AI Yin Xiaowai WeChat Channels QR code"></a>
    </td>
  </tr>
</table>

Personal column: https://waytoagi.feishu.cn/wiki/Pddywh6NqiRKb4kaJBscAbf9nUA

---

![Photo Poetic Postcard](assets/images/banner.svg)

# Photo Poetic Postcard | Cross-Agent Skill

[中文](README.md)

![Agent Skill](https://img.shields.io/badge/Agent-Skill-C46A32?style=flat-square)
![One Photo One Result](https://img.shields.io/badge/One%20Photo-One%20Result-D97706?style=flat-square)
![Model Adaptive](https://img.shields.io/badge/Model-Adaptive-A16207?style=flat-square)
![Content License](https://img.shields.io/badge/Content-CC%20BY--NC--SA%204.0-2F2A25?style=flat-square)

Turn one user photo into one finished poetic postcard: preserve the original photograph above, reinterpret only one extracted subject below, then add restrained typography and three sampled color swatches.

The workflow is not tied to a single image model and never requires four candidates. It can be installed as a Skill, pasted as a standalone prompt, or degraded honestly when the host lacks image tools.

## Gallery

These are verified outputs made from authorized source photos in one complete image-generation operation. No lower panel was generated separately, and no typography was added later with code. All six results measure `1086 × 1448`, exactly 3:4. Use the source links below to inspect how each main subject was extracted; see [examples/README.md](examples/README.md) for the case record.

<!-- GALLERY:START -->
<table>
  <tr>
    <td width="33%" align="center"><img src="examples/gallery/results/case-01-xiaoqikong-result.webp" alt="Xiaoqikong poetic postcard result"><br><strong>01 · Xiaoqikong</strong><br><a href="examples/gallery/sources/case-01-xiaoqikong-source.webp">View source</a></td>
    <td width="33%" align="center"><img src="examples/gallery/results/case-02-shaolin-result.webp" alt="Shaolin Temple poetic postcard result"><br><strong>02 · Shaolin Temple</strong><br><a href="examples/gallery/sources/case-02-shaolin-source.webp">View source</a></td>
    <td width="33%" align="center"><img src="examples/gallery/results/case-03-kitten-result.webp" alt="Kitten poetic postcard result"><br><strong>03 · Kitten and corn</strong><br><a href="examples/gallery/sources/case-03-kitten-source.webp">View source</a></td>
  </tr>
  <tr>
    <td width="33%" align="center"><img src="examples/gallery/results/case-04-golden-hall-result.webp" alt="Golden Hall poetic postcard result"><br><strong>04 · Golden Hall</strong><br><a href="examples/gallery/sources/case-04-golden-hall-source.webp">View source</a></td>
    <td width="33%" align="center"><img src="examples/gallery/results/case-05-portrait-result.webp" alt="Portrait poetic postcard result"><br><strong>05 · Waterside portrait</strong><br><a href="examples/gallery/sources/case-05-portrait-source.webp">View source</a></td>
    <td width="33%" align="center"><img src="examples/gallery/results/case-06-riverside-result.webp" alt="Riverside boat poetic postcard result"><br><strong>06 · Riverside boat</strong><br><a href="examples/gallery/sources/case-06-riverside-source.webp">View source</a></td>
  </tr>
</table>
<!-- GALLERY:END -->

## Highlights

- One source photo produces one final deliverable.
- The upper photograph fills its region edge to edge by default, with no paper margin or border; ratio mismatches use a restrained cover crop.
- The lower panel extracts one subject instead of repainting the complete scene.
- It follows DECONSTRUCT → SELECTIVE PRESERVATION → DISTILL → RECONSTRUCT, keeping only the subject and zero to three directly attached identity cues while removing the recognizable environment.
- Model-adaptive: Image Gen, Dreamina, Doubao, or any other provider may be used when actually available.
- Honest fallback: a vision-only Agent returns one fully resolved prompt; a no-vision Agent does not invent the image.
- Standalone Chinese and English Prompt MD files work when Skills cannot be installed.
- Place evidence is resolved before copywriting; a confirmed place must appear verbatim in the title or note, while uncertain locations are never guessed.
- Users may customize dimensions, split ratio, medium, layout, typography, paper, swatches, and color treatment.
- The upper photograph, lower reinterpretation, paper, typography, swatches, and layout are generated together in one image operation; no later stitching or programmatic typesetting is allowed.

## Compatibility

| Platform / context | Recommended setup | Image output |
| --- | --- | --- |
| Codex / ChatGPT desktop | Install the standard Skill | Depends on image tools available in the current session |
| Claude Code | Copy to personal or project Skills | Depends on connected model, MCP, or image tool |
| WorkBuddy | Upload the dedicated ZIP | Depends on the selected workspace model or connector |
| Gemini CLI | Install from Git | Depends on current tool configuration |
| Other `SKILL.md` Agents | Install or copy the standard package | Depends on host capabilities |
| Dreamina / Doubao image Agents | Paste a standalone Prompt MD | Usually runs inside the product's native image workflow |
| Basic image generators | Upload the photo and paste the prompt | Yes, if reference-image input is supported |

Skill installation and image-generation capability are separate. This repository defines the workflow; it never pretends that a missing host tool exists.

See [Installation and Compatibility](docs/INSTALLATION_EN.md) for details.

## Method 1: install as an Agent Skill

### Codex

Ask `$skill-installer`:

```text
Install the Skill from https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.
```

Or clone it manually:

```bash
git clone https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git ~/.agents/skills/xiaowai-photo-poetic-postcard
```

### Claude Code

Personal installation:

```bash
git clone https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git ~/.claude/skills/xiaowai-photo-poetic-postcard
```

For project scope, place it at `.claude/skills/xiaowai-photo-poetic-postcard/`.

### Gemini CLI

```bash
gemini skills install https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard.git --consent
```

### WorkBuddy

Download `xiaowai-photo-poetic-postcard-workbuddy.zip` from GitHub Releases and upload it through WorkBuddy's Skill creation/import flow. The archive uses the required `skills/<skill-name>/SKILL.md` structure and WorkBuddy-specific bilingual metadata.

Then upload a photo and ask:

```text
Use xiaowai-photo-poetic-postcard to turn this photo into one poetic postcard.
```

## Method 2: use the Prompt MD directly

If your Agent cannot install Skills, upload the photo and paste one complete file:

| Language | File |
| --- | --- |
| Chinese | [references/photo-poetic-postcard-prompt.zh-CN.md](references/photo-poetic-postcard-prompt.zh-CN.md) |
| English | [references/photo-poetic-postcard-prompt.en.md](references/photo-poetic-postcard-prompt.en.md) |

This is the recommended route for Dreamina, Doubao, and other image-capable Agents without a documented GitHub Skill installer.

See the [resolved Xiaoqikong example](references/example-xiaoqikong-compiled-prompt.zh-CN.md) to understand what a fully compiled image-model prompt looks like. Its place, subject, colors, and copy are example-specific and must not be reused for other photos.

> **Paste the complete file and do not let an intermediary Agent summarize it.** Before calling an image model, the instructions require a concrete extracted subject, a photo-specific omission list, exact copy, three colors, and resolved layout positions. A one-paragraph prompt that merely says “keep the photo above and repaint the same scene below” indicates a failed handoff; stop and use the complete file again.

## Why this version is more robust across Agents

The standalone prompt is an end-to-end execution contract rather than a set of style keywords:

1. The default 3:4 canvas is strictly divided into two independent 50% regions.
2. The main Skill embeds the complete Chinese downstream template, so success does not depend on the host following a reference link.
3. The Agent must resolve one concrete subject and a photo-specific omission list; “the whole landscape” or “the same scene” is invalid.
4. The final image-model prompt must preserve all five sections and may not be summarized into one paragraph.
5. The three swatches have a testable size rule: each is a perfect solid square about `1/20` of lower-panel width.
6. Generation is blocked until the prompt includes every required section, subject, omission, exact copy, three colors, and delivery constraint.

## Capability fallback

| Host capability | Behavior |
| --- | --- |
| Vision + image generation | Generate and deliver one final image |
| Vision, no image generation | Analyze the source and return one resolved, model-ready prompt |
| No vision | State the missing capability and do not invent the source image |

## User-adjustable controls

| Control | Default | Examples |
| --- | --- | --- |
| Canvas | 3:4, 1080 × 1440 | 4:5, 1:1, 9:16, custom pixels |
| Panel split | Strict 50/50 | Explicitly adjustable to about 40–65%; the Agent must not drift automatically; photo remains flush to top and side edges |
| Medium | transparent watercolor, light gouache, colored pencil | ink wash, printmaking, paper collage, restrained digital paint |
| Subject scale | moderately compact and complexity-aware | horizontal/detailed subjects about 55–70% lower width; people, animals, and rings about 40–55% |
| Subject position | negative-space driven | left, center, or right, while keeping at least about 45% visibly clean paper |
| Paper | warm ivory fiber | cool gray-white, handmade fiber, smooth museum stock |
| Text | Chinese title + short note | custom language/typeface or no text |
| Swatches | three, grouped in a clear lower-panel corner | reposition or hide; if shown, keep three perfect solid squares, each about 1/20 of lower-panel width |
| Color | sampled, muted | warmer, cooler, monochrome accent while source-traceable |
| Layout | resolved after placing the subject | move text and swatches among lower-panel corners; avoid repeating one fixed arrangement |

## Validate and package

```bash
python tools/validate_repo.py
python tools/build_packages.py
```

The build produces a standard Agent Skills ZIP and a WorkBuddy ZIP under `dist/`.

## License

- Skill instructions, prompts, visual-system documentation, READMEs, and other written content: **CC BY-NC-SA 4.0**. Attribution, noncommercial reuse, adaptation, and sharing are permitted; adaptations must use the same license. Commercial use requires separate permission.
- Code under `tools/`: **MIT License**.
- Author identity assets, the WeChat QR code, and source/result images under `examples/`: excluded from the open licenses and provided for project presentation only unless a file says otherwise.

See [LICENSE](LICENSE), [LICENSE-CODE](LICENSE-CODE), and [NOTICE.md](NOTICE.md). Because the core prompt content is noncommercial, “openly shared” is more precise than strict open-source software; the MIT-licensed code is open source.

## Feedback

Issues and Discussions are welcome. Before sharing a public example, confirm that you have the necessary rights to the source photo and any recognizable person in it.
