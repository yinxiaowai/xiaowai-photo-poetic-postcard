---
name: xiaowai-photo-poetic-postcard
description: Turn one user photo into one finished poetic postcard in a single image-generation operation, with a faithful photographic upper panel and a watercolor reinterpretation of exactly one extracted subject below. Use for literary travel postcards, photo-and-illustration split compositions, or customizable variations of this visual system.
---

# Photo Poetic Postcard

Create one complete postcard from one source photo. Produce the upper photograph, lower reinterpretation, paper, title, note, and layout together in one image-generation operation. Never generate separate pieces, stitch panels, or add typography with code afterward.

## Critical execution rule

This Skill is not only an art-direction reference. It is a **downstream prompt compiler**.

Before every image-generation call, analyze the source, resolve the content card, compile the complete Chinese prompt defined below, and send that full prompt to the image model **verbatim** with the source image attached. 不得概括、缩写、转述或压缩成一段普通风格描述。A one-paragraph prompt that merely says “keep the photo above and repaint the same scene below” is invalid because it loses the panel lock, subject extraction, omit list, whitespace, and typography constraints.

If the host exposes a separate image-tool prompt field, put the complete compiled prompt in that field. Do not replace it with a short summary. If the host can only hand work to another Agent, return the complete compiled prompt unchanged so the user can paste it directly.

## Detect host capability

Choose the truthful path:

1. **Vision + image generation:** inspect the source, compile the full prompt, attach the source, and generate the integrated postcard.
2. **Vision without image generation:** inspect the source and return a compact analysis, resolved parameter card, and the complete compiled prompt. State that no image was generated.
3. **No vision:** state that image understanding is required. Direct the user to the [standalone Chinese prompt](references/photo-poetic-postcard-prompt.zh-CN.md) or [English prompt](references/photo-poetic-postcard-prompt.en.md) in an image-capable Agent. Never invent the subject, colors, place, or composition.

Do not require a specific vendor or model. Use the strongest reference-image generation or editing capability actually available.

## Resolve one content card

Read the [standalone Chinese drawing guide](references/photo-poetic-postcard-prompt.zh-CN.md) or [English drawing guide](references/photo-poetic-postcard-prompt.en.md) in full before generation. Each contains the complete selection, composition, customization, and correction method and works without this entrypoint. The [visual system](references/postcard-design.md) is an optional compact reference. Inspect the photo and resolve every applicable field:

- `main_subject`: exactly one visual center to reinterpret, never “the whole scene”;
- `identity_cues`: zero to three features belonging to, touching, or directly interacting with that subject;
- `omit_list`: concrete visible nouns that must disappear from the lower panel;
- `photo_subject` and `key_relations`: facts the upper photo must preserve;
- `complexity`, `medium`, `subject_scale`, and `subject_position`;
- exact `title` and `note` text;
- `typography`: one concrete, scene-matched type treatment with readable strokes and spacing, chosen automatically unless specified by the user;
- `place_name`, evidence source, and confidence;
- exact lower-panel positions for the subject and text group;
- output ratio or dimensions and panel split.

Resolve place identity in this order: a name explicitly supplied by the user; legible signage, EXIF, or geotag; then a uniquely identifiable landmark only at high confidence. If confirmed, the exact place or landmark name must appear verbatim in the title or note. If evidence is insufficient, use scene-based copy and never guess.

Default to one exact 3:4 portrait image, strict 50/50 upper/lower regions, warm low-saturation ivory fiber paper, transparent watercolor plus light gouache and a trace of colored pencil, one concise Chinese title, one natural Chinese note. Honor explicit user changes to dimensions, split, medium, paper, scale, position, language, typography, copy, palette, or layout while preserving the core invariants.

Paper and breathing room apply only to the lower panel. The upper photo has zero margins: it covers the full canvas width from the top edge to the panel boundary. Never interpret “postcard paper” as an outer mat around the photograph or the whole work.

## Mandatory downstream prompt contract

### Copy and adaptive typography

For automatically composed Chinese copy, prefer common simplified characters, familiar words, and natural short phrases. Avoid rare or unnecessarily dense glyphs used only for ornamental literary effect; do not impose an arbitrary stroke-count cap or ban all complex characters. Preserve confirmed names and user-supplied wording exactly, simplifying only surrounding original copy.

Actively choose typography from the photo's subject, mood, illustration medium, and text density. There is no default Song font. Everyday life, pets, and relaxed portraits may suit clear natural handwriting; historic architecture may suit restrained regular script or serifs; contemporary scenes may suit humanist sans. These are possibilities, not fixed mappings or random font rotation. Handwriting needs no explicit user request. Honor explicit font choices. Prioritize distinguishable glyphs, complete strokes, and comfortable spacing; avoid tangled cursive, broken strokes, ultra-thin small text, and excessive font mixing. Resolve one concrete treatment in the image prompt, not a list of alternatives or merely “use a suitable font.” Do not claim exact font-file fidelity without verification.

Copy and typography rules are pre-generation decisions. This workflow does not require post-generation OCR, typo detection, text correction, or typo-triggered retries.

### Compile the prompt

Use the detailed drawing guide to make decisions first; the block below is only the image-tool handoff format, not a substitute for the guide. Fill every brace with image-specific content. Remove braces before sending. Keep the five section headings and all applicable constraints. For Chinese-capable image Agents such as Dreamina or Doubao, use this Chinese prompt directly. For an English-only image model, translate the filled content without deleting or merging sections.

Apply explicit user overrides before compiling: omit text and its checks when no text is requested; replace the Chinese-only restriction when another language is requested; resolve a custom split or ratio consistently throughout the prompt. Remove the conditional place-name sentence when no place is confirmed. Choose subject scale by shape, not by a single universal percentage. Keep a naturally cropped source subject rather than inventing unseen anatomy or structure to complete its silhouette.

```text
【画面结构】
根据上传的唯一一张原图，生成一张完整的{画布比例或像素尺寸；默认精确3:4竖版}诗意明信片。整张画布严格水平分成上下两个独立区域，默认上下等高、各占50%；只有用户明确指定其他比例时才允许改变。绝对不允许整张图全部转绘：上半区必须保留原摄影，下半区才做艺术转绘。上方照片、下方转绘、纸张、标题、短注和全部排版必须在同一次生图中一次性生成；禁止先生成局部后拼接，禁止事后用程序排字。所有文字100%限制在下半区，不能进入上半区。最终只交付一张完整成品，禁止主动生成四种风格、四张候选、四宫格、对比图或单独的下半图。

【上半区｜原摄影锁定】
上方满版、下方留白，两个区域不可混用留白规则。摄影必须覆盖从整张画布顶部到上下分界线的完整横向矩形，照片底边直接抵达分界线，无纸条、无分隔描线；不是把照片缩小后摆在纸面上。纸张肌理与留白只在下半区，不能形成整图米白外框。
上半区使用上传的原摄影，原图主体为{photo_subject}，关键空间与视觉关系为{key_relations}。以cover方式铺满整个上半区，贴齐整张画布顶部、左边和右边，不留纸边、白边、描边、轮廓线、边框、相框或阴影。只允许为铺满上半区进行必要的等比裁切；不得拉伸，不得生成式扩图，并应保住主要主体。完整保留原图的主体、光影、色彩、空间关系和摄影质感，不得重画、替换、美化、修饰、增删或改写任何摄影内容。上半区除原摄影外绝对不能出现文字或其他元素。

【下半区｜单一主体转绘】
只提取并转绘{main_subject}，不是把整幅原图、同一场景或完整背景再画一遍。仅保留这些最低必要辨识线索：{identity_cues；没有则写“无额外线索”}。明确省略并禁止出现：{omit_list，必须写成与本图对应的具体可见对象}。采用“拆解 → 选择性保留 → 蒸馏 → 重构”，以{medium}表现主体的轮廓、结构、材质和关键配色。主体约占下半区宽度{subject_scale；按主体形状选择}，放在{subject_position}，该位置根据下方文字和留白独立确定，不照搬原图坐标或强制上下居中对齐；保持完整自然轮廓，边缘自然消融进纸面，不触碰下半区左右边缘或下边缘。下半区至少保留约45%连续、明显、干净的纸面，密度介于“孤立小图标”和“完整场景水彩”之间。主体后方采用连贯的半透明环境色水彩晕染，从轮廓向上方及两侧自然散开，深浅不均、湿边渗化、外围淡入纸面；不是只在脚下画一条承托。晕染与主体形成一个整体，保留周围安静纸面；不得形成可识别背景、第二场景、矩形图块或第二主体。

【文字与排版】
文案已优先选用常见、自然、易辨认的字词；已确认地名及用户指定原文不作简写或替换。下述字体是根据本图内容、气质和文字密度选定的具体方案，不统一套用宋体；字形清楚、笔画完整、间距舒展，手写风格也不能连笔到难以辨字。
标题严格写作“{title}”，短注严格写作“{note}”，采用{typography和language}，逐字准确，只出现一次。若地点或景点已确认，准确名称“{place_name}”必须在标题或短注中原样出现；未确认时不得编造。文字组仅放在下半区的{text_position}。文字是安静的小注记，不是海报大标题；标题字高约为整图宽度的3%—4%，短注约2.4%—3%，随实际字数微调且保持可读，不抢插画主体。文字组根据真实负空间安排，可位于下半区左上、右上、左下或右下，不得遮挡主体，也不得固定所有作品都使用同一角落。

【禁止项与交付】
禁止下半区完整场景复刻，禁止保留{omit_list}，禁止上半摄影被转绘，禁止上半区出现文字，禁止外框、照片边框、阴影、悬浮卡片、Logo、签名、水印、英文或任何未指定文字。检查实际像素比例、上下分区、原摄影保真、单一主体提取、具体省略项、留白。不要求生成后识别错字、纠字或因文字重试。上述构图项失败都应在生图阶段修复同一张完整作品，不得改用拼接或程序排字。最终仅展示并交付一张通过检查的完整成品。
```

## Downstream prompt preflight

Do not invoke the image tool until the compiled prompt passes every item:

Check the active brief: text items below apply only when enabled, and default geometry phrases are replaced by explicit user settings. A user's valid customization must not fail a default-only check.

- contains all five exact section headings;
- contains `上下两个独立区域` and the resolved split, defaulting to `上下等高、各占50%`;
- explicitly locks the photo to the canvas top, left, right, and panel boundary with zero paper margins or outlines, and confines paper and breathing room to the lower panel;
- identifies one concrete `main_subject`; “same scene,” “whole landscape,” or an unresolved placeholder is not valid;
- contains `只提取并转绘` followed by that concrete subject;
- contains a concrete `omit_list` naming visible background elements from this photo;
- contains the exact resolved title, note, and text position;
- when text is enabled, resolves one scene-matched type treatment and checks original copy for avoidable glyph complexity without altering confirmed names or user wording;
- contains the one-shot ban on stitching and programmatic typography;
- contains `最终只交付一张` and does not request styles or candidates;
- contains no unresolved `{placeholder}`.

If anything is missing, repair the prompt before generation. Never rely on the image model to infer an omitted rule from the Skill name or a previous message.

## Subject extraction rules

Use `DECONSTRUCT → SELECTIVE PRESERVATION → DISTILL → RECONSTRUCT`:

- **Architecture or bridge:** keep the structure and at most three identifying cues. A bridge may keep a minimal water echo directly inside or beneath its openings; omit the broad river, forest, mountain, sky, distant buildings, roads, crowds, and unrelated trees.
- **Person:** keep identity-defining facial structure, hair, clothing, and key pose; omit the recognizable location and broad landscape.
- **Animal with an interacting object:** keep the animal and only the object it directly touches when that relationship is essential; omit the surrounding floor, yard, buildings, and clutter.
- **Plant, ring, or installation:** keep its silhouette, material, and signature colors; omit lawn, sky, lamps, paths, and background structures.
- **Vehicle or boat:** keep the vehicle and only a tight grounding shadow or reflection; omit the town, skyline, mountain, broad water, and waterfront.

The lower result must read as one illustrated subject on paper, not a second rectangular picture, filtered thumbnail, or watercolor copy of the full photograph.

## Composition rules

- The source photo fills the upper region edge to edge and touches the top and both side edges. No paper gap, hairline, border, outline, frame, or generative extension.
- Its bottom edge meets the panel boundary directly, without a paper strip or divider stroke. Reject a photograph inset on a paper mat, even if the lower illustration is correct.
- Compose the lower panel independently: preserve the extracted subject's identity and structure, not its source-photo coordinates or center alignment. Arrange its scale and left/center/right position with the text and breathing room. Detailed horizontal subjects normally use about 55%–70% of lower width; people, animals, rings, and compact objects normally use about 40%–55%.
- Keep at least about 45% of the lower panel visibly quiet. Remove environmental cues before enlarging the design.
- Place the exact title/note only after reading actual negative space. Do not default every result to lower-right.

## Generation and correction

Attach the original photo and send the complete compiled prompt in one call. Do not generate the lower panel separately. Do not use a local compositor. Do not overlay title, note, borders, or layout with code after generation.

Do not ask for four styles or multiple candidates. If the host automatically returns multiple images despite a one-image request, inspect them, select at most one compliant result, and present only that result. A correction is a retry of the same final work, not an additional candidate.

If ratio, extraction, or photo fidelity fails, correct the same complete design through image generation while restating the full contract. If the host cannot preserve the upper photograph, state the limitation and recommend a stronger reference-image model rather than silently switching to a stitched workflow.

## Acceptance checklist

Apply this checklist to the resolved brief: disabled text must be absent, and explicit custom geometry replaces the defaults.

- One exact requested-ratio image; for the default, width divided by height equals 0.75. A 2:3 result fails.
- Strict upper/lower regions at the resolved split; default is 50/50.
- Upper region is the faithful original photograph, full-bleed at top and sides.
- Lower region contains exactly one extracted subject and no recognizable full-scene background.
- The concrete omit list is absent from the lower panel.
- Subject remains contained and at least about 45% of the lower paper is visibly quiet.
- Title and note are placed only in the lower panel; spelling and confirmed-name preservation are specified before generation, not post-generation OCR checks.
- No extra text, logo, signature, watermark, border, shadow, grid, comparison, or candidate sheet.
- Every visible component was generated together; the delivered artifact is one image only.
