# CelebClock AI Image Workflow

Use this workflow for every source image.

## Developer process order
1. Load candidate image as the clock background.
2. Find fingertip, mark it with a green circle, and get developer corrections/approval.
3. Crop according to developer direction.
4. Resize and determine the minute alignment.
5. Correct hour/minute alignment on the clock.
6. Test by toggling Test/Auto mode and confirming marker placement.
7. Update JSON fields (`minute`, `filename`).
8. Rename the image file in `imgs/` (or `imgs/temp/` while in-progress) to match JSON.

## Feedback iteration sequence
- fingertip -> crop -> resize -> correct hour -> test
- after each step, collect developer feedback and iterate before continuing
- final sync must keep JSON and image filename aligned

## Default behavior
- If no correction is provided after fingertip review, continue with the current fingertip mark.
- If no correction is provided after red-target review, continue with the current red marker and save.

## Temp image workflow
- Use `imgs/temp/` as the first working location for all in-progress image edits.
- Save the untouched source as `MM-celebname-orig.jpg` in `imgs/temp/`.
- Keep all intermediate temp images for developer inspection.
- Do not delete temp images unless the developer explicitly instructs deletion.
- When asked to crop, preserve the celebrity in frame; choose crop direction by where the subject is located so the person remains in the picture.

## Missing minutes
- For minutes with no candidate source image, generate candidate prompts and mark `status: missing_source`.
- After generation, re-enter the same review flow beginning at step 1.
