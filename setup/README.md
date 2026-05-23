# Setup Folder

This folder contains Node.js scaffolding for the celeb image workflow.

## Contents
- `data/celebMinutes.js`: minute-sorted celeb source records.
- `js/workflowState.js`: workflow step definitions and result-table template.
- `js/runWorkflow.js`: builds a minute-by-minute next-action summary.
- `js/nonRepeatingPicker.js`: picks celebs without repetition in each round.
- `ai-instructions.md`: review loop instructions for green/red marker approvals.

## Run
```bash
cd setup
npm run workflow:summary
```
