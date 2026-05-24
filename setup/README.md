# Setup Folder

This folder contains Node.js scaffolding for the celeb image workflow.

## Contents
- `data/celebMinutes.json`: minute-sorted celeb source records.
- `js/workflowState.js`: workflow step definitions and result-table template.
- `js/runWorkflow.js`: builds a minute-by-minute next-action summary.
- `js/nonRepeatingPicker.js`: picks celebs without repetition in each round.
- `ai-setup-instructions.md`: iterative review loop with step-versioning (`v1.01.n`), fingertip approval flow, crop approval gates, and test-mode marker rules (green approved fingertip, optional blue initial).

## Run
```bash
cd setup
npm run workflow:summary
```
