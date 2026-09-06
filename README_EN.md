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

Turn one user photo into one finished poetic postcard: preserve the original photograph above and reinterpret only one extracted subject below, with restrained typography in the same generated work.

The workflow is not tied to a single image model and never requires four candidates. It can be installed as a Skill, pasted as a standalone prompt, or degraded honestly when the host lacks image tools.

## Gallery

These six authorized source/photo-postcard pairs demonstrate subject extraction, outward watercolor washes, scene-matched typography, and independent lower-panel layouts. Use the source links below to compare content choices; see [examples/README.md](examples/README.md) for the case record.

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
- Users may customize dimensions, split ratio, medium, layout, typography, paper, and color treatment.
- The upper photograph, lower reinterpretation, paper, typography, and layout are generated together in one image operation; no later stitching or programmatic typesetting is allowed.

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

No project installation or repository-homepage access is needed. Upload a photo and send the online MD link directly to the Agent. If it cannot read URLs, download and attach the MD, or paste its full text.

Current release: **v1.3.0**. Online links pin that release; download links follow GitHub's latest stable Release.

| Language | Current release online MD (send to an Agent) | Latest release MD (download and attach) |
| --- | --- | --- |
| Chinese | [Complete Chinese guide · v1.3.0](https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard/blob/v1.3.0/references/photo-poetic-postcard-prompt.zh-CN.md) | [Download Chinese MD](https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard/releases/latest/download/photo-poetic-postcard-prompt.zh-CN.md) |
| English | [Complete English guide · v1.3.0](https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard/blob/v1.3.0/references/photo-poetic-postcard-prompt.en.md) | [Download English MD](https://github.com/yinxiaowai/xiaowai-photo-poetic-postcard/releases/latest/download/photo-poetic-postcard-prompt.en.md) |

Old version links stay old: copy the current link from this page when updating. No URL can forcibly clear a third-party Agent's cache. Download and attach the MD if it still reads stale content. See [Version and update notes](docs/PROMPT_VERSIONS.md).

This is the recommended route for Dreamina, Doubao, and other image-capable Agents without a documented GitHub Skill installer.

Each file is a self-contained **15-section drawing guide** covering image roles, subject selection and omission, subject-specific decisions, panels, crop conflicts, media, scale and whitespace, paper and washes, place evidence and copy, typography, customization, host capabilities, correction, and delivery. No template fields or other repository files are needed.

Ask the Agent to process your photo using the attached guide. It decides unspecified layout, copy, colors, and brushwork from the image. Add adjustments in ordinary language, such as “make the lower area airier, use light ink.”

The [Xiaoqikong example](references/example-xiaoqikong-compiled-prompt.zh-CN.md) is optional reading to illustrate one application. It is not required for Method 2, and its place, copy, and colors are specific to that photo.

### Jimeng: generate only, or generate and add a reusable skill

The [Chinese README's Method 2 examples](README.md#方式二把-md-当作完整提示词直接使用) include two copy-ready prompts reported as successful by the user in Jimeng: generation only, and generation followed by a native “添加技能” card for user confirmation. Both explicitly override v1.3.0's single-result default with four independent 3:4 candidates using 图片 5.0 Lite. All four retain the same core subject and vary the lower composition, typography, and washes; they are not a four-panel image. These are platform-specific usage requests, not changes to the model-neutral drawing guide or a promise of GitHub installation support in every Agent.

## Cross-Agent execution design

The guide explains decisions; the main Skill's five-section template conveys resolved instructions to a separate image model. Method 2 contains everything it needs independently:

1. The default 3:4 canvas is strictly divided into two independent 50% regions.
2. The main Skill embeds the Chinese handoff template and requires reading the complete drawing guide; Method 2 needs no other files.
3. The Agent must resolve one concrete subject and a photo-specific omission list; “the whole landscape” or “the same scene” is invalid.
4. Image-tool calls preserve sections and all active requirements while resolving observations into specific decisions; no lossy summary.
5. Pre-generation checks follow active requirements; explicit no-text and language choices update the defaults and checks together.

These are execution rules and design goals, not evidence of successful testing in every Agent or image model. Repository validation checks documents and packages; visual behavior still needs testing in the target environment.

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
| Typography | Agent-selected from image content, mood, and medium; no default Song font | handwriting, regular script, rounded, serif, or sans; readability first; user-overridable |
| Color | sampled, muted | warmer, cooler, monochrome accent while source-traceable |
| Layout | resolved after placing the subject | move text among lower-panel corners; avoid repeating one fixed arrangement |

Original copy favors common characters and natural short phrases without altering confirmed names or user wording. Typography selection is active by default: users need not request a font change, and the Agent should not use rigid subject-to-font mappings or random rotation.

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
