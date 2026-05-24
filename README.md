# CelebClock

Celebrity image clock.

## What The App Does
- Shows an analog clock.
- Replaces minute hand with a celebrity image pointing to the active minute.
- Picks from minute-mapped celebrity entries.
- Supports non-repeating celeb rotation per round.

## Screenshot
![CelebClock screenshot](imgs/celebclockscreenshot.jpg)

## Data
- Main minute records: [setup/data/celebMinutes.json](setup/data/celebMinutes.json)
- Redundant celeb-to-minutes map: [setup/data/celebs.json](setup/data/celebs.json)
- Downloaded/local images: [imgs/](imgs)

## Current Dataset Snapshot
- Minutes covered in JSON: 0, 7, 8, 9, 10, 13, 15, 16, 18, 19, 30, 40, 45.
- Only one entry marked downloaded: minute 7 (Muhammad Ali).
- Other minutes are pending source rows.

Dev stages and development workflow notes are in [ai/development.md](ai/development.md).
