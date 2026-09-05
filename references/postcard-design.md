# Poetic Postcard Visual System

This reference defines the stable design language and the parameters users may change. The rules are model-neutral.

## Content card

Resolve these once before generating:

| Field | Default | Decision rule |
| --- | --- | --- |
| Main element | One visual center | Choose the most recognizable subject, not the whole scene |
| Identity cues | 0–3 | Keep only features attached to or directly interacting with the subject |
| Omit list | Required | Name the background scenery and clutter that must disappear |
| Complexity | Detailed / simple | Use it to set subject scale and whitespace |
| Place evidence | Name + source + confidence | User statement > legible sign/EXIF/geotag > uniquely identifiable landmark with high confidence |
| Title | Confirmed place name or scene-based Chinese title | A confirmed place must appear verbatim in the title or note; otherwise never guess |
| Note | 6–10 Chinese characters | Quiet, natural postcard tone; no invented facts |
| Colors | Three sampled colors | Distinct, representative, fixed order |
| Canvas | 3:4 portrait | Use the user's ratio or dimensions when provided |
| Panel split | Strict 50 / 50 | Default to two equal independent regions for maximum cross-model reliability; change only when the user explicitly asks |
| Rendering | Transparent watercolor + light gouache + colored pencil | Replace or blend only when the user requests another medium |

If the user supplies title or note text, preserve it exactly. If the user requests no text or no swatches, remove that system and rebalance the whitespace.

## Place and title evidence

Determine location before writing the copy:

1. Treat an explicit place or landmark name supplied by the user as authoritative for the current task.
2. Otherwise use a legible sign, EXIF, or geotag from the source photo.
3. Otherwise name a uniquely identifiable landmark only when confidence is high.
4. If the location is confirmed, include its exact name at least once in the title or note. Poetic wording may support the name but must not replace it.
5. If evidence is insufficient or ambiguous, use scene-based copy and do not guess.

Record the evidence source and confidence in the content card. Visible text can establish the photographed subject, such as a clearly readable plaque, but do not infer a broader city or region that the evidence does not establish.

## Main-element extraction

Extraction uses `DECONSTRUCT → SELECTIVE PRESERVATION → DISTILL → RECONSTRUCT`. It means recognizing the photo's visual center, deleting background noise, and redrawing only the selected subject with the minimum cues needed for identity:

- **Architecture:** preserve one to three distinctive identity cues such as roofline, opening, arch, tower, or facade rhythm; remove crowds, roads, sky, trees, distant scenery, and surface ornament not required for recognition.
- **Person:** preserve identity-defining facial structure, hair, clothing, and key pose; omit the recognizable setting and use at most one localized abstract color wash.
- **Plant or installation:** preserve silhouette, material, and signature colors; omit lawn, sky, fixtures, and background structures.
- **Landscape:** choose one explicit landmark or core natural form. A bridge means the bridge and a minimal water echo, not the forest, trees, mountain, and full river scene.
- **Vehicle or boat:** keep the vehicle plus only the shadow or reflection that directly grounds it; omit the town, skyline, mountain, and broad environment.
- **Simple symbol or ring:** reduce scale and increase breathing room so the form does not become heavy.

The subject needs a complete, natural silhouette with watercolor edges dissolving into paper. It must not look like a second rectangular picture or a miniature copy of the original scene. Immediate props that physically interact with the subject may remain when removing them would change the subject relationship, such as corn held by a kitten.

## Composition system

### Default geometry

- One portrait canvas, normally 3:4.
- Upper and lower regions share one horizontal axis, default to two equal 50% regions, and are generated as one integrated composition.
- The photo fills the upper region edge to edge and touches the canvas top, left, and right edges. There is no paper margin, hairline, outline, border, or frame around it.
- Its bottom edge meets the panel boundary without a paper strip or divider stroke. Paper texture and breathing room belong only to the lower region; never place a smaller photo on an ivory mat around the whole composition.
- Use cover-style cropping when source and target ratios differ. Crop only what is necessary, preserve the main subject, never stretch the photo, and never invent an extension.
- The lower main element stays contained and never touches the edges. Position it left, center, or right according to its silhouette and the available negative space.
- Preserve at least about 45% of the lower panel as visibly quiet paper. Horizontal or detailed subjects may use about 55–70% of lower-panel width; people, animals, rings, and compact subjects normally use about 40–55%.
- The desired density is slightly fuller than a sparse isolated cutout but clearly lighter than a full-scene watercolor. Add only one localized wash or one directly attached cue; never reconstruct a recognizable environment.

### Lower-panel layers

Use only these layers:

1. paper field;
2. one faint irregular translucent wash;
3. one extracted main element and minimal cues;
4. optional title and note;
5. optional three-color swatch group.

Do not add geometric collage, large opaque blocks, decorative stickers, drop shadows, a second focal point, or unrelated ornaments.

## Adjustable parameters

| Parameter | Safe range or examples | Preserve |
| --- | --- | --- |
| Canvas | 3:4, 4:5, 1:1, 9:16, custom pixels | One coherent composition |
| Photo share | Default exactly 50%; user-adjustable about 40–65% | Photo and illustration must both remain legible; do not vary automatically |
| Medium | watercolor, ink wash, colored pencil, printmaking, collage-like paper grain, restrained digital paint | Lower panel remains a reinterpretation of one photo-derived element |
| Subject scale | compact, balanced, moderately expansive | Match complexity; keep at least one broad continuous area of clean paper |
| Subject position | left, center, right; slightly high or low | Keep intentional whitespace |
| Paper | warm ivory, cool gray-white, handmade fiber, smooth museum stock | Quiet low-contrast field |
| Text | custom title/note, another language, no text | Exact spelling; no extra copy |
| Typography | modern Song/serif, sans, handwritten, supplied font | Legibility and hierarchy |
| Swatches | reposition, recolor from photo, hide | If shown, exactly three solid squares; each side is about 1/20 of lower-panel width |
| Color | faithful, muted, warmer, cooler, monochrome accent | Traceable to source; avoid arbitrary palette replacement |
| Layout | subject may shift left/center/right; text and swatch group may use any lower-panel corner | Choose from actual negative space; do not repeat one default layout |

## Prompt blocks

### Complete full-image prompt

Use this structure for a reference-image model:

```text
Create one finished {canvas ratio or dimensions} poetic postcard from the attached source photo in one image-generation operation. Divide it into two independent horizontal regions, defaulting to an exact 50/50 split unless the user explicitly changes it. Generate the upper photo region, lower reinterpretation, paper, typography, color swatches, and complete layout together. Do not generate separate panels and do not rely on later compositing or text overlay.

[Upper region — source photo lock]
Fill the upper {photo share} of the canvas edge to edge with the source photo. The photo must touch the canvas top, left, and right edges with no paper margin, hairline, outline, border, or frame. Use cover-style cropping only as needed to fit the region; preserve the main subject, never stretch the photo, and never generatively extend it. Preserve the photo's subject, lighting, color relationships, spatial relationships, and photographic character. Do not redraw, replace, beautify, retouch, or add anything to the photograph.

[Lower region — one extracted subject]
Apply DECONSTRUCT → SELECTIVE PRESERVATION → DISTILL → RECONSTRUCT. Reinterpret only {main element}. Preserve only {zero to three attached identity cues}. Explicitly omit {background omit list}. The lower illustration must not reproduce a recognizable environment or become a miniature of the source photo. Render it in {medium}. Keep a complete natural silhouette with edges dissolving into paper; do not use a rectangular image tile, border, shadow, or floating card. {scale and position instruction}. Preserve at least about 45% visibly quiet paper. Add at most one localized, soft, irregular, translucent wash, never a second scene or focal point.

[Typography and palette]
Write the title exactly as “{title}” and the note exactly as “{note}” in {typography/language}. When {confirmed place} is available, its exact name must appear verbatim in the title or note. Place the text in {text position chosen from negative space}. Add exactly three equal, tiny, solid-color square swatches sampled from the photo — {hex colors} — as one compact group at {a different clear corner when possible}. Each square's side is about 1/20 of the lower-panel width, with a perfectly uniform flat fill and no texture, image content, gradient, circle, or irregular shape. Text and swatches may use upper-left, upper-right, lower-left, or lower-right within the lower panel; do not always default to the same pair. Do not add any other text, number, logo, signature, or watermark.

[Art direction]
Use {paper} and {color treatment}. Keep the result quiet, airy, contemporary, and editorial. Return one complete image only.
```

## Failure recovery

- **Upper photo changed:** strengthen reference-image fidelity and edit the same complete design; if the host still cannot preserve it, disclose the limitation rather than switching to a stitched workflow.
- **Whole scene repeated below:** name the single subject and explicitly list the omitted environment.
- **Panel feels too full:** remove environmental cues first, then reduce the subject and wash until at least about 45% clean paper remains.
- **Layout feels repetitive:** move the subject, copy, and swatch group according to actual negative space; keep each group separate and vary valid arrangements across a gallery.
- **Subject too large:** switch from expansive to compact scale and increase whitespace.
- **Wrong text:** repeat the exact text and typography constraints in a targeted full-image correction; never add replacement text programmatically.
- **Swatches become photo fragments:** specify solid fill, equal small squares, no texture or gradient, and correct the complete image in the generation stage.
- **Model returns multiple options:** repeat “one complete final image only” and discard grids or candidate sheets.
- **Wrong canvas ratio:** inspect pixel dimensions and correct the same complete design in the image-generation stage. Do not crop or resize the final artwork with code.
- **Agent shortens the prompt:** do not generate. Recompile the mandatory five-section prompt from `SKILL.md`, resolve every placeholder, and send it verbatim.
