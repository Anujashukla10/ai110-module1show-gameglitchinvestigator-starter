# 🎮 Game Glitch Investigator: The Impossible Guesser
#done


## 🚨 The Situation


You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.


- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.


## 🛠️ Setup


1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`


## 🕵️‍♂️ Your Mission


1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!


## 📝 Document Your Experience


- [ ] Describe the game's purpose.
Glitchy Guesser is a number guessing game where the player tries to guess a secret number within a limited number of attempts. It supports three difficulty levels (Easy, Normal, Hard) with different number ranges and attempt limits, and tracks a score that decreases with wrong guesses.


- [ ] Detail which bugs you found.
1. Inverted hints - "Go HIGHER!" appeared when the guess was too high, and "Go LOWER!" when too low - exactly backwards.
2. String vs integer comparison - on even-numbered attempts, the secret was converted to a string, causing lexicographic comparisons where "85" < "9" would flip the result.
3. Hard difficulty easier than Normal - Hard used range 1–50, which is a smaller target space than Normal's 1–100, making it easier despite fewer attempts.
4. Attempts started at 1 - session state initialised attempts = 1, silently burning the first guess before the player did anything.
5. New Game didn't reset status - after winning or losing, clicking New Game left status as "won" or "lost", so the game over screen persisted.
6. Hardcoded range in UI - the info banner always displayed "1 to 100" regardless of the selected difficulty.


- [ ] Explain what fixes you applied.
1. Flipped the hint logic in check_guess() — guess > secret now correctly returns "Go LOWER!".
2. Removed str(secret) conversion — secret stays an integer throughout, eliminating the lexicographic comparison bug entirely.
3. Corrected Hard range to 1–200 in get_range_for_difficulty().
4. Reset attempts to 0 in the new centralised reset_game() function.
5. reset_game() now clears status, so New Game always returns to a clean playing state.
6. Info banner now uses {low} and {high} pulled dynamically from get_range_for_difficulty().


## 📸 Demo Walkthrough


Describe your fixed game in numbered steps so a reader can follow along without watching a video:


1. Start game at normal difficulty (8 attempts)
2. Player guesses 50 -> "Go Higher" (secret is above 50)
3. Player guesses 75 -> "Go Lower" (secret is below 75)
4. Player guesses 62 -> "Go Lower" (score drops by 5 for every wrong guess)
5. Player guesses 58 -> "Go Higher"
6. Player guesses 60 -> Correct and the Ballons appear
7. Final score dislays, which is higher because it was solved in 5 attempts
8. Player clicks New Game and the status clears, attempts reset to 0




**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->


## 🧪 Test Results


```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```


## 🚀 Stretch Features


- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]





