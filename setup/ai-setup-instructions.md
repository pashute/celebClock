# CelebClock AI Image Workflow

Use this workflow for every source image.

## Workflow versioning
- During in-progress step work, use patch versions with step suffixes: `v1.01.1`, `v1.01.2`, `v1.01.3`.
- Each completed step increments the trailing `.n` by 1.
- When the full flow is approved/finalized, remove the trailing `.n` and bump main version: `v1.01.n -> v1.02`.

## Approval gate (mandatory)
- Every step requires explicit developer approval before moving to the next step.
- AI must stop after each step, ask for approval/corrections, and only then continue.

## Step notification
- After each completed step, run `tput bel` three times in terminal (`tput bel; tput bel; tput bel`).
- Also print a visible terminal line before/after the bell sequence so completion is visible even if sound is muted.

## Developer process order
1. Load candidate image as the clock background.
2. Find fingertip with an initial estimate and collect developer corrections/approval.
3. After fingertip approval, update JSON (`origFingertipCoord`, `origFingertipMinute`) and clear `initial` to empty string (`""`) so blue marker no longer shows in test mode.
4. Propose crop plan and ask developer for approval before cropping.
5. Crop according to approved direction, ensuring the approved green fingertip marker remains inside the crop.
6. Ask developer if anything else should be cropped out; iterate until approved.
7. Resize if needed, modify minute assignment if needed, and get developer approval before continuing.
8. Correct hour/minute alignment on the clock.
9. Test by toggling Test/Auto mode and confirming marker placement; in test mode, the approved fingertip marker shows in green.
10. Apply final circle-crop polish so the final image looks clean inside the clock.
11. Update JSON fields (`minute`, `filename`) and any approved marker/alignment values.
12. Rename the image file in `imgs/` (or `imgs/temp/` while in-progress) to match JSON.

## Feedback iteration sequence
- fingertip (initial+corrections) -> fingertip approval+JSON update -> crop proposal+approval -> crop+extra-crop check -> resize+minute adjust -> correct hour -> test -> final circle-crop polish
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
