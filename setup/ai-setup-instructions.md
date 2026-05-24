# CelebClock AI Image Workflow

Use this workflow for every source image.

## Required sequence
1. Load candidate image behind the clock as a background layer.
2. Mark the fingertip/point target with a green circle.
3. Ask the developer for approval or directional correction.
4. Resize/crop/reposition image to align with the selected minute.
5. Mark the expected minute target with a red circle.
6. Ask the developer for final approval.
7. Persist result row into JS data table with filename, minute, approvals, and notes.

## Default behavior
- If no correction is provided after step 3, continue with current fingertip mark.
- If no correction is provided after step 5, keep the current red marker and move to save state.

## Missing minutes
- For minutes with no candidate source image, generate candidate prompts and mark `status: missing_source`.
- After generation, re-enter the same review flow beginning at step 1.
