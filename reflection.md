# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The hints were weird, even when I guessed 100 it told me to go higher when I guessed 1 it told me to go lower. The new game button did not work, so I had to refresh the browser. When I pressed the new game button the number of attempts went up to 8. Developer info score and final score were shown differently.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 5 | Go higher | Go lower | None |
| 100 | Go lower | Go higher | None |
| 61 | Go higher | Go lower | None |
| 63 | Go lower | Go higher | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude code for help on this project. All the suggestions AI gave me was pretty much correct. Some of the suggestions were more than what I was asking for but overall for this project it worked. It properly fixed the High/Low logic error as well as the new game error. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

The best way to ensure the bug was fixed was to actually play the game afterwards. Also I manually verified the changes before I allowed the AI to make the changes. I had to make sure it was targetting the right areas and changing the proper things. AI helped me design and run a final test after the alterations. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit is a python framework to build web applications that are dynamic and interactive. Its helpful to make small interactive sites that operate with data. Session state helps retrive user data across the web application.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I would like to keep checking AI's work for accuracy just to ensure I am making the right changes. Next time I could be a bit more specifc or descriptive in my prompts. This project was the first time I worked simultaneously with AI to edit/generate code so I thought it was a very interesting and cool experience watching it not only make suggestions but to be able to go and make changes as well. 