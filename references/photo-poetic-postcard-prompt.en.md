# Photo Poetic Postcard | Standalone English Prompt

If your Agent cannot install Skills, upload one source photo and paste this file into an Agent that can understand and generate images. The default output is one final image.

## Optional settings

Leave a field unchanged to use its default:

- Canvas: `[3:4 portrait, 1080 × 1440]`
- Panel split: `[strict 50/50; change only when explicitly requested]`
- Rendering medium: `[transparent watercolor + light gouache + a trace of colored pencil]`
- Paper: `[warm, low-saturation ivory fiber paper]`
- Place evidence: `[fill when known; an explicit user-supplied name takes priority]`
- Title: `[a confirmed place must appear verbatim in the title or note; otherwise derive from the scene and never guess]`
- Note: `[one short natural line]`
- Typography: `[contemporary serif, strong title and lighter note]`
- Subject scale: `[moderately compact, with at least about 45% visible clean paper]`
- Layout: `[adapt to actual lower-panel negative space; do not lock text lower-left and swatches lower-right]`
- Swatches: `[three sampled colors grouped in one clear lower-panel corner; each square about 1/20 of lower-panel width]`
- Other requirements: `[none]`

## Complete instruction to paste into an Agent

```text
Inspect the single source photo I uploaded before doing anything else. Treat it as the only factual and visual source. This entire code block is the final execution instruction. If you call a separate image model, pass every section and rule to it without summarizing, shortening, merging, or paraphrasing them into a one-paragraph style description. Never replace “extract one subject” with “repaint the same scene.”

[Capability check]
If you can inspect and generate or edit images, first resolve the subject, concrete omission list, colors, copy, and layout, then send this complete instruction to the image model and create exactly one finished image in one image-generation operation. Do not write a shorter tool prompt. If you can inspect the photo but cannot generate images, return one fully resolved, copyable prompt that preserves every section and contains the specific subject, omission list, colors, title, note, and settings; state clearly that you did not generate an image. If you cannot inspect the photo, state that image understanding is unavailable and do not invent its subject, colors, location, or composition.

[Canvas structure]
Turn the source into one complete 3:4 portrait poetic postcard. Divide the complete 3:4 canvas strictly into two equal, independent horizontal regions, 50% each by default; change this split only when I explicitly request it. Never reinterpret the whole canvas: the upper region must remain the original photograph and only the lower region is illustrated. Generate the upper photo, lower reinterpretation, paper, title, note, three swatches, and full layout together in one image-generation operation. Do not generate separate pieces, stitch panels, or overlay text or swatches with code afterward. Keep 100% of typography and swatches in the lower region. Return one image only — do not request multiple styles, a candidate set, four-up grid, comparison sheet, or isolated lower panel.

[Analyze and lock]
Apply DECONSTRUCT → SELECTIVE PRESERVATION → DISTILL → RECONSTRUCT. Choose exactly one concrete main element from the photo; “the whole landscape,” “the same scene,” and “the entire photo” are not subjects. Keep only zero to three minimum identity cues that belong to, touch, or directly interact with that subject, and create a concrete omission list using visible nouns from this photo. Remove background noise, distance, sky, forest, mountains, streets, crowds, and low-information decoration; do not retain a recognizable setting merely to make the result richer. Before calling the image model, the final prompt must literally identify the concrete extracted subject and the concrete omitted objects rather than generic placeholders. Sample three distinct representative colors from the photo. Create a concise title and a short natural note. Resolve place evidence in this order: a place or landmark name explicitly supplied by me; a legible sign, EXIF, or geotag in the source; then a uniquely identifiable landmark only when confidence is high. If a place is confirmed, its exact name must appear verbatim at least once in the title or note and must not be replaced by generic poetic copy. If evidence is insufficient, use scene-based copy and never guess a place, attraction, or building.

[Upper panel — source photo lock]
Fill the upper region edge to edge with the source photo using cover-style cropping. The photograph must touch the canvas top, left, and right edges with no paper gap, white margin, hairline, outline, border, or frame; never shrink it into a floating card. When ratios differ, crop only what is needed to fill the region, keep the main subject, never stretch the photo, and never generatively extend it. Preserve the photographic subject, lighting, color relationships, spatial relationships, and photographic character. Do not redraw, replace, beautify, retouch, add, or alter photographic content.

[Lower panel — one extracted subject]
Reinterpret only the selected concrete main element rather than repainting the whole photograph, the same scene, or the complete background. Preserve its identifying silhouette, structure, material, and key colors, plus no more than three cues that directly touch or interact with it. A bridge keeps the bridge and only a minimal water echo near its arches, not the forest, trees, mountain, or full river; a boat keeps the boat and a tight reflection, not the town, mountain, or waterfront; a person keeps the person and defining clothing/pose, not a recognizable scenic background. Use transparent watercolor layers, light gouache, and a trace of colored pencil by default. Preserve a complete natural silhouette with edges dissolving into paper. Do not use a rectangular tile, outline, frame, shadow, or floating card. Position the subject left, center, or right according to its shape. Default subject width is about 55–65% of the lower panel; horizontal or detailed subjects may use about 55–70%, while people, animals, rings, and compact subjects normally use about 40–55%. Keep at least about 45% visibly clean continuous paper. The desired density is between a sparse isolated icon and a full-scene watercolor. Place at most one localized soft irregular translucent wash behind the subject; it must not become a background scene or second focal point.

[Typography and swatches]
Use a contemporary serif by default, with one concise title and one lighter short note on two horizontal lines. Spell all text exactly. Lay out the subject first, then place the text group in an actual negative-space area at the upper-left, upper-right, lower-left, lower-right, or side of the lower panel. Place exactly three equal, tiny, perfect solid-color square swatches sampled from the photo as one compact horizontal group in a clear lower-panel corner, preferably separate from the text group. Each square's side is about 1/20 of the lower-panel width, and each fill is 100% uniform and flat. Do not always default to lower-left text and lower-right swatches; vary valid arrangements across multiple examples. Keep both groups clear of the subject. Do not put swatches in the photo or render them as photo fragments, textures, patterns, gradients, circles, irregular shapes, or a fourth swatch.

[Overall direction]
Use warm, low-saturation ivory fiber paper. Keep the result airy, quiet, poetic, refined, and contemporary-editorial. Do not frame the whole canvas. Apart from the requested title and note, add no other words, numbers, logo, signature, or watermark.

[User-controlled adjustments]
If I specify a different canvas ratio or dimensions, panel split, medium, subject scale or position, paper, title, note, language, typeface, swatch position, color treatment, or removal of text/swatches, prefer my settings. Still preserve these invariants: the source photo is the sole source, the upper photograph receives no semantic alteration, the lower panel reinterprets one subject only, and the final delivery is one complete image.

[Prohibitions and delivery]
Before generation, verify that the image-model prompt still contains the full Canvas structure, Upper panel, Lower panel, Typography and swatches, and Prohibitions and delivery sections; a concrete subject; a concrete omission list; exact copy; three concrete colors; resolved text and swatch positions; three perfect squares sized at 1/20; and one-image delivery. Do not generate when any item is missing. Before delivery, inspect the actual pixel dimensions: the default width-to-height ratio must equal exactly 3:4; 2:3 is not acceptable, and the default panel split is exactly 50/50. Verify that the upper photo was not redrawn or replaced; the lower panel contains only one subject and minimum attached cues rather than a full-scene copy; the concrete omitted objects are absent; at least about 45% of the lower paper remains visibly clean; subject, text, and swatches use composition-aware negative space; a confirmed place appears verbatim at least once in the title or note while no place is invented when unconfirmed; text is accurate; swatches have the right count, size, and shape; and there is no extra copy, logo, watermark, frame, shadow, or multi-image output. Repair the same complete work only within the image-generation stage; never crop, stitch, or typeset it with code. Show only one compliant final image.
```

## Using a basic image generator

If a tool accepts only an image and a prompt, upload the photo and paste the code block above. If it cannot perform the analysis step, first ask a vision-capable Agent to identify the main element, three colors, title, and note, then replace the generic fields with those concrete details.
