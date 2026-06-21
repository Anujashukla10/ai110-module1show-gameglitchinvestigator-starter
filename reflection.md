# 💭 Reflection: Game Glitch Investigator


#done


Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.


## 1. What was broken when you started?


- What did the game look like the first time you ran it?
    -It gives the wrong hints and it looks like AI generated as it doesn't have any theme.


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    - attempts number is shown wrong on the website
    - it says you already won start a new game, but doesn't change anything when I start a new game.
    - the numbers are not in range according to difficulty
    - attempts left is wrong


**Bug Reproduction Log**


Document at least 3 bugs you found. Add rows as needed.


| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|15 |Go Higher |Go Lower |Give opposite hints |
|85 |Go Higher |Go Lower |the attempts number is wrong |
|66 |Go Lower |Go Higher |new game doesn't start |


---


## 2. How did you use AI as a teammate?


- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used mix of chatgpt and claude for this project


- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude was able to give the correct code for the new game button, hints and the attempts. I first compared what code the claude changed, asked it how the code that it changed worked and then tried the website with multiple inputs.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude gave me the correct code however when I ran the code it changed the whole layout (UI) of the project. so I had to tell it to change the theme back to how the project looked like.




---


## 3. Debugging and testing your fixes


- How did you decide whether a bug was really fixed?
I tried the website multiple times with correct, incorrect guesses and also tried new game option once I won the game.


- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
test_too_high_hint_says_go_lower, guessed 60 against a secret of 50, confirmed the message contained "LOWER" and not "HIGHER". This directly proved the inverted hint bug was fixed.


- Did AI help you design or understand any tests? How?
Yes, I described the bugs in chat and the AI translated each one into a focused pytest case. For example, I knew the hints were backwards but didn't think to test the string-vs-int edge case ("85" < "9") until the AI pointed out that was the root cause of the even-attempt bug, not just a side effect. It also suggested testing parse_guess with None and float strings, which I wouldn't have covered on my own


---


## 4. What did you learn about Streamlit and state?


- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?


---


## 5. Looking ahead: your developer habits


- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.





