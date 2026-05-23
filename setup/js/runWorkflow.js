import { createDefaultResultTable, workflowSteps } from "./workflowState.js";

export function nextActionForEntry(entry) {
  if (!entry.approvedGreenMarker) {
    return workflowSteps[1];
  }
  if (!entry.approvedRedMarker) {
    return workflowSteps[4];
  }
  return workflowSteps[6];
}

export function buildWorkflowSummary() {
  const table = createDefaultResultTable();
  return table.map((entry) => ({
    minute: entry.minute,
    celeb: entry.celeb,
    nextAction: nextActionForEntry(entry),
    status: entry.status
  }));
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const summary = buildWorkflowSummary();
  console.log(JSON.stringify(summary, null, 2));
}
