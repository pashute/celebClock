# AI Development Instructions
- The code assistant AI should read this file first thing after recovery


- Before every action by AI, the AI should put a telegraphic summary in `ai/chatHistory.md` with a bulleted chckbox and datetime-stamped format for each line, as follows:

- [ ] yyyy/mm/dd-hh:mm:  action-summary. 

- These include code changes, git and github actions. calls to we and server etc.   
- Always save after every edit to `ai/chatHistory.md` file, so it is preserved after a crash. 
- Mark each completed item with:
 - [v] success, [x] cancelled, [-] deferred, [?] needs developer attention.

NO INSTRUCTIONS by the developer should be done without first listing it in the `ai/chatHistory.md`

EVERY INSTRUCTION should be listed (and timestamped) in the chatHistory.md file.
EVERY CHANGE should be recorded. 

The developer does not need to remind the AI to record the instructions. 

Instruction changes and new instructions should be modified or recorded in the chat history, even if they are remarks and interuptions in the middle of a larger or different task. 

Bottom line:  EVERYTHING SHOULD BE RECORDED AND SAVED. 

#Checking in

When committing and pushing use a commit message with telegraphic text to discribe all the changes in markdown. Give it a headline (cosmetics: changed a -> b)  etc. 

Give a short list of files affected, in the commit message. 

List the commit headline (not the details) in the chatHistory.md


RECORD EVERYTHING YOU DO AND SAVE THE HISTORY!