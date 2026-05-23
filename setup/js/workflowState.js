import { celebMinuteEntries } from "../data/celebMinutes.js";

export const workflowSteps = [
  "Load source image as clock background",
  "Mark fingertip with green circle",
  "Request developer approval/correction",
  "Resize and reframe image while preserving clock target",
  "Mark expected target minute with red circle",
  "Request developer approval",
  "Store finalized metadata in result table"
];

export function createDefaultResultTable() {
  return celebMinuteEntries.map((entry) => ({
    minute: entry.minute,
    celeb: entry.celeb,
    filename: entry.filename,
    sourceUrl: entry.sourceUrl,
    downloaded: entry.downloaded,
    approvedGreenMarker: false,
    approvedRedMarker: false,
    status: "pending",
    notes: ""
  }));
}
