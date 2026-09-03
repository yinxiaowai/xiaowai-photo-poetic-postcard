---
name: xiaowai-photo-poetic-postcard
description: Turn one user photo into one finished poetic postcard in a single image-generation operation, with a faithful photographic upper panel and a watercolor reinterpretation of one extracted subject below. Use for literary travel postcards, photo-and-illustration split compositions, or customizable variations of this visual system.
---

# Photo Poetic Postcard

Create one complete postcard from one source photo. The entire composition must be produced in one image-generation operation: upper photograph, lower reinterpretation, paper, title, note, swatches, and layout. Do not assemble separate panels or add text programmatically afterward.

## Start with capability detection

Determine which path the current host supports:

1. **Full-image generation path:** the host can inspect the source and generate or edit an image from a reference. Generate the complete postcard once as one integrated image. If it fails quality review, repair the same design and return only the final corrected image.
2. **Prompt handoff path:** the host can inspect the photo but has no image-generation capability. Analyze the photo and return one complete, model-ready prompt containing the image-specific subject, colors, title, note, and requested parameters. Do not claim that an image was generated.
3. **No-vision path:** the host cannot inspect the photo. Explain that image understanding is required. Direct the user to [the standalone Chinese prompt](references/photo-poetic-postcard-prompt.zh-CN.md) or [English prompt](references/photo-poetic-postcard-prompt.en.md) in an image-capable Agent. Never invent the photo's subject, colors, place, or composition.

Do not require a specific vendor or model. Use the best reference-image generation or editing capability actually available in the current host.

## Resolve the brief

Read [the visual system](references/postcard-design.md) before generating.

Honor explicit user choices. For anything not specified, use these defaults:

- output: one 3:4 portrait image;
- split: upper photo about 48%, lower design about 52%;
- paper: warm, low-saturation ivory fiber paper;
- reinterpretation: transparent watercolor, light gouache, and a trace of colored pencil;
- text: one concise Chinese title and one natural Chinese note;
- palette: exactly three small square swatches sampled from the photo;
- layout: place subject, text, and swatches after inspecting the lower panel's negative space; do not lock them to one repeated arrangement.

The user may adjust the aspect ratio or dimensions, photo/illustration ratio, rendering medium, subject scale and position, paper treatment, title, note, language, typography, swatches, color treatment, and lower-panel arrangement. If an adjustment conflicts with a core invariant, preserve the invariant and explain the smallest necessary compromise.

## Analyze once

Create one internal content card before generation:

- one main element to reinterpret;
- zero to three minimum identity cues that belong to or directly touch that subject;
- an explicit omission list for the rest of the scene;
- complexity: detailed or simple;
- title and short note;
- place evidence, evidence source, and confidence;
- three distinct representative colors in fixed order;
- output ratio, panel split, style, scale, and layout;
- whether the place identity is certain enough to name.

Resolve place identity in this order: an explicit place name supplied by the user; a legible sign, EXIF, or geotag in the source; then a uniquely identifiable landmark only when confidence is high. Treat a user-supplied place name as authoritative for the current task. If a place or landmark is confirmed, its exact name must appear verbatim at least once in the title or note; do not replace it with generic poetic copy. If evidence is insufficient, write a natural scene-based title and never guess a landmark.

## Generate the complete image once

Send the source photo as the reference image and request one complete, integrated postcard. The generation prompt must define all parts together:

1. one 3:4 portrait paper canvas;
2. the source photograph filling the upper region edge to edge, flush with the top and both side edges, with no paper margin and no hairline;
3. one extracted main element reinterpreted in the lower region;
4. one optional soft, irregular translucent wash;
5. exact title and note text in the clearest lower-panel corner or side space;
6. exactly three sampled solid-color square swatches grouped in a different clear lower-panel corner when possible;
7. no additional text, object, logo, signature, watermark, candidate, or separate panel.

Do not generate the lower panel separately. Do not use a local compositor. Do not overlay title, note, swatches, borders, or layout with code after generation. “One input → one output” means one complete integrated design, not a stitched artifact.

Use `DECONSTRUCT → SELECTIVE PRESERVATION → DISTILL → RECONSTRUCT` for the lower illustration. Keep the selected subject and only its minimum attached identity cues. Remove recognizable background scenery, distant architecture, broad landscape, sky, forest, cliffs, streets, crowds, and decorative clutter. A faint irregular color wash may echo the source palette, but it must not reconstruct a second scene.

Compose adaptively rather than by template:

- anchor the illustration left, center, or right according to its silhouette and the available negative space;
- place the title/note group in whichever lower-panel corner or side space balances the subject;
- place the three-swatches group in another clear corner; do not default every result to lower-right;
- for a multi-example gallery, deliberately vary valid arrangements across cases;
- keep at least about 45% of the lower panel as visibly quiet paper. Horizontal or detailed subjects may use about 55–70% of lower-panel width; people, animals, rings, and compact objects normally use about 40–55%.

If the first generation fails, use a targeted correction while restating all invariants. A correction is a retry of the same final work, not a second candidate. Show only one accepted result to the user.

## Prompt handoff path

Return:

1. a compact photo analysis;
2. the resolved parameter card;
3. one complete copyable full-image prompt;
4. a short note naming the missing capability and where the prompt can be used.

Do not output several prompt variants unless the user explicitly asks for alternatives.

## Core invariants

- Use the uploaded photo as the sole factual and visual source.
- Generate every visible component together in the image-generation stage.
- The upper panel uses a cover-style crop: fill its full width and height, touch the canvas top, left, and right edges, and leave no paper gap, border, outline, or frame. Never shrink the photograph into a floating card.
- Crop only as needed to fill the upper region. Do not stretch or generatively extend the photo; keep the main subject and essential visual relationships intact.
- The upper panel must look like the original photograph and preserve its subject, lighting, color relationships, spatial relationships, and photographic character. Do not replace, expand, repaint, beautify, or add content.
- The lower panel reinterprets exactly one main element, not the entire scene.
- Keep only minimum cues physically attached to or immediately interacting with the subject. Do not preserve a recognizable environmental background merely for atmosphere.
- Keep the lower illustration contained rather than filling the whole lower region. Preserve at least one broad continuous area of untouched paper for typography and visual breathing room.
- Keep a complete natural silhouette; never place the illustration inside a rectangular photo tile, frame, shadow, or floating card.
- Use at most one soft, irregular, translucent wash behind the subject.
- If swatches are enabled, use exactly three equal, small, solid-color squares sampled from the source photo.
- Add no fabricated location, extra object, English copy, number, logo, signature, or watermark unless the user explicitly requests it.
- Never omit a confirmed place or landmark in favor of generic poetic copy; include its exact name in the title or note.
- Deliver one complete final image.

## Acceptance checklist

- The result is one organically designed image, not two separately generated images stitched together.
- Typography, swatches, borders, and layout were generated as part of the same image operation.
- The upper photo remains visually faithful, fills its region edge to edge, and has not been replaced with an illustration.
- No white or paper margins, hairlines, borders, or frame surround the upper photograph.
- The two regions feel intentionally balanced at the chosen ratio.
- The lower region contains one extracted subject rather than a second full-scene painting.
- Subject scale matches its complexity, stays visually contained, does not touch the edges, and leaves intentional negative space for copy and swatches.
- Title and note are accurate and spelled exactly as resolved.
- If the place or landmark was confirmed, its exact name appears at least once in the title or note; if it was not confirmed, no place name was invented.
- Swatch count, shape, color, and position match the brief.
- No unintended frame, shadow, extra text, logo, watermark, or duplicate composition appears.
- The delivered artifact is one image only.
- The actual pixel dimensions match the requested aspect ratio. For the default, width divided by height must equal 0.75 (3:4); a 2:3 output is not acceptable.
- Text and swatches occupy composition-aware negative space rather than repeating the same lower-left/lower-right template in every result.

If text is wrong, correct the same complete image through another image-generation edit. Never replace the failed text with a programmatic overlay. If the model cannot keep the upper photo sufficiently faithful, state that limitation and recommend a stronger reference-image model rather than silently switching to a stitched workflow.
