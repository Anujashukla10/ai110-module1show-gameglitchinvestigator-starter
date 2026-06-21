#done
# import random
import streamlit as st


from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)




# ── Helpers ────────────────────────────────────────────────────────────────────


def reset_game(difficulty: str):
    lo, hi = get_range_for_difficulty(difficulty)
    # FIX: AI identified that New Game never cleared `status`, so "You already
    # won" persisted forever. Centralised all reset logic here so both first
    # load and New Game behave identically. Collaborated via chat-mode prompting.
    st.session_state.secret   = random.randint(lo, hi)
    # FIX: AI spotted attempts was initialised to 1, silently burning the first
    # guess before the player did anything. Reset to 0 here and in init below.
    st.session_state.attempts = 0
    st.session_state.score    = 0
    st.session_state.status   = "playing"
    st.session_state.history  = []




# ── Page config ────────────────────────────────────────────────────────────────


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")


st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")


# ── Sidebar ────────────────────────────────────────────────────────────────────


st.sidebar.header("Settings")


difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)


attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]


low, high = get_range_for_difficulty(difficulty)
# FIX: Hard was returning 1–50 (easier than Normal's 1–100). I caught this
# and asked AI to fix it; range corrected to 1–200 in logic_utils.py.


st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")


# ── Session state init ─────────────────────────────────────────────────────────


if "secret" not in st.session_state:
    reset_game(difficulty)


# ── Main UI ────────────────────────────────────────────────────────────────────


st.subheader("Make a guess")


# FIX: Banner was hardcoded to "1 to 100" regardless of difficulty.
# I asked AI to fix it. now uses {low}/{high} pulled from get_range_for_difficulty().
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)


with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)


raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)


col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)


# FIX: Old New Game block was hardcoded to randint(1,100) and never reset
# `status`. AI refactored this to call reset_game() instead.
if new_game:
    reset_game(difficulty)
    st.success("New game started.")
    st.rerun()


if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()


if submit:
    ok, guess_int, err = parse_guess(raw_guess)


    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)


        # FIX: Original code converted secret to str() on even attempts, causing
        # lexicographic comparison bugs (e.g. "85" < "9"). I told AI that this is causing the issue and AI identified this as
        # the root cause of random wrong hints. Removed entirely; secret stays
        # int throughout. Logic extracted to logic_utils.py.
        outcome, message = check_guess(guess_int, st.session_state.secret)


        st.session_state.attempts += 1


        if show_hint:
            st.warning(message)


        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )


        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )


st.divider()
st.caption("Built by an AI that claims this code is production-ready.")

