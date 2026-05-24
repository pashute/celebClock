AI chat history.  for recovery from Codespaces carshes.  
- The code assistant AI should read this file first thing after recovery!

# Instructions

- Before every action by AI, the AI should put a telegraphic summary here, in following bulleted chckbox and datetime-stamped format:

- [ ] yyyy/mm/dd-hh:mm:  action-summary. 

- These include code changes, git and github actions. calls to we and server etc.   
- Always save after every edit to this file, so it is preserved after crash. 
- Each completed item mark with:
 - [v] success, [x] cancelled, [-] deferred, [?] needs developer attention.


# Log

- [v]  Add first fingertip circle marker to SVG and report coordinates (cx=463, cy=67).
- [v]  Start local server first in separate terminal tab/session and open preview tab (http://localhost:5500).
- [v]  Commit and push latest changes as requested (commit 131f1f7 to origin/main).
- [v]  Start server again in separate terminal tab and open preview tab.
- [v]  User confirmed fingertip marker is correct.
- [v] Add hour-circle direction marker based on center-to-fingertip vector and report coords (cx=393, cy=128).
- [ ] Wait for user directional correction for hour-circle marker.
- [v] Apply latest request: red target and resize-to-align while keeping marker coordinates fixed.
- [v] Wait for user approval of resize result.
- [v] After approval only: add third circle on outer tick-edge circle and crop image to circular boundary.
- [v] User requested immediate crop: circle boundary at outside end of red dot (applied crop radius 197 from center).
- [v] Remove green fingertip dot, then commit and push (dot removed).
- [v]  Add celebshot screenshot to README using imgs/celebClockScreenshot.jpg.
- [v]  Clarified screenshot filename preference to celebclockscreenshot; update README/path accordingly.
- [v]  Commit and push screenshot rename + README path update (commit ae92105).
- [v]  Wait for new instructions
- [v] 2026/05/23-20:49: Read chat history and follow last instruction.
 - [ ] dateAndTimestamp these instructions here. 
- [ ] see temp.md, (i'll soon update it further but don't wait for that). 
 - [ ] check in and push to github
  - [ ] consolidate all readme lists by minute starting at 0.  
  - [ ] each celeb has a category (art, government, etc.) 
  - [ ] url column (as a link), 
  - [ ] and copywrite name and link.  
  - [ ] If UNKONWN copywrite, then mark it thus. 
  - [ ] filename (give each a simple filename 1elvis.jpg  etc)
  - [ ] checkbox if downloaded. We only have the single image for minute 7.
  - [ ] make a setup folder with .js (nodejs?) that with following modules: 
    - [ ] ai instructions .md file (for each image put as background in clock, mark fingertip with green circle, get approval from developer or corrections, get next step instructions (default: mark with red circle expected target minute after resizing image.
    get developer's approval. store results in a data table in the js folder  (js objects and arrays). 
    - [ ] use ai to create the images for missing minutes, and the resized image, cropping out (with the developer's instructions) unneeded parts of the picture colorizing and correcting so we can use a picture as is.  for the minute. 
    - [ ] the program itself would be a simple one, choosing one out of set of celebs (and next round without repeating the celebs).
    - [ ] empty the temp.md
    - [ ] change the readme to reflect all we said. remove any unnecessary and old instructions. 
- [ ] commit and push all to github. 
- [v] 2026/05/23-22:40: Read instruction markdown and execute pending checklist items.
- [v] 2026/05/23-22:40: Rewrite README with consolidated minute-sorted table and metadata columns.
- [v] 2026/05/23-22:40: Create setup Node.js scaffolding, AI workflow instructions, and JS data table files.
- [v] 2026/05/23-22:40: Empty temp.md and remove stale plan content.
- [v] 2026/05/23-22:40: Commit and push updates to origin/main.
- [v] 2026/05/23-22:44: Committed and pushed changes (a577c88) to origin/main.
- [v] 2026/05/24-00:01: Migrated celeb minute data from JS to JSON, preserved latest entries, and updated workflow/doc references.
- [v] 2026/05/24-00:09: Added .vscode/settings.json to version control and pushed commit ac78d0e to origin/main.
- [v] 2026/05/24-00:19: Logged request to split README/dev docs, create redundant celebs JSON, and verify old minute knowledge coverage.
- [v] 2026/05/24-00:24: Rewrote README app-first, moved dev notes to ai/development.md, added setup/data/celebs.json, spaced celebMinutes.json entries, and verified old minute mappings remain in git history.