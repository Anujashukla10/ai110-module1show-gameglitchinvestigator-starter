def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200      # FIX: was 1–50, which was easier than Normal
    return 1, 100


# done


def parse_guess(raw: str):
    """
    Parse user input into an int guess.


    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."
    if raw == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    return True, value, None




def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).


    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: hints were inverted AND secret is always int (no str() conversion)
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"   # FIX: was "Go HIGHER!"
    return "Too Low", "📈 Go HIGHER!"        # FIX: was "Go LOWER!"




def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points
    if outcome == "Too High":
        return current_score - 5
    if outcome == "Too Low":
        return current_score - 5
    return current_score



