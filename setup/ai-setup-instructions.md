# CelebClock AI Image Workflow

Use this workflow for every source image.

## Developer process order
1. Load candidate image as the clock background.
2. Find fingertip, mark it with a green circle, and get developer corrections/approval.
3. Crop to fingertip only if the developer instructs that crop.
4. Resize and determine the new minute.
5. Mark the expected minute target with a red circle and get final developer approval.
6. Update JSON minute listing and filename.
7. Rename the image file in `imgs/` (or `imgs/temp/` while in-progress) to match JSON.

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
