AI chat history.  for recovery from Codespaces carshes. 

- Before every action by AI, the AI should put a telegraphic summary here.   
- These include code changes, git and github actions. calls to we and server etc.   
- Always save after every edit to this file, so it is preserved after crash. 

Developer's latest prompt (he entered it here because needs to go and will come back later. its a workflow)

read ai chat history md file
then , while recording your actons,
1. put a small bright circle on his fingertip location. 
2.  tell me location coords of that circle in image. 
3. I will correct you and tell you right left up down till we get it correctly. 
4. once we have the fingertip, we do a similar correction session (back and forth) with another circle on the hour circle in the direction from the center to the fingertip on the hour circle. 
5. Once i confirm it correct you tell me how much you think to resize and what it will do to the minute pointed at
6. Once i confirm you resize
7. Run the server in a SEPARATE TAB. you keep on overriding the codespaces tab, and then its gone and i have to re-run codeespaces, which of course brings us back to point zero after a crash!!

Updated workflow (2026-05-21, per user correction)
1. Run server first in a separate terminal tab/session and open site in separate browser tab.
2. Put a small bright circle on his fingertip location.
3. Tell location coords of that circle in image.
4. User gives right/left/up/down corrections until fingertip is correct.
5. After fingertip is confirmed, do similar correction loop for another circle on the hour circle in the direction from center to fingertip.
6. Once hour circle is confirmed, estimate resize amount and effect on minute pointed at.
7. Once confirmed, apply resize.


Line format:
- [ ] timestamp action-summary. 

- [v] 2026-05-21 Read latest instructions from this file and begin workflow.
- [v] 2026-05-21 Inspect project files and image assets to locate fingertip.
- [v] 2026-05-21 Read page code and add first bright fingertip marker.
- [v] 2026-05-21 Add first fingertip circle marker to SVG and report coordinates (cx=463, cy=67).
- [ ] 2026-05-21 Wait for user directional correction (left/right/up/down) for fingertip marker.
- [ ] 2026-05-21 Start local server first in separate terminal tab/session and open preview tab.
- [ ] 2026-05-21 Commit and push latest changes as requested.