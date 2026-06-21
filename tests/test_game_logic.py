from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# ── check_guess: outcomes ───────────────────────────────────────────────────────

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# ── BUG 1: hints were inverted ──────────────────────────────────────────────────
# Original returned "Go HIGHER!" when guess > secret, and "Go LOWER!" when guess
# < secret — exactly backwards. These tests fail on the buggy version.

def test_too_high_hint_says_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_hint_says_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


# ── BUG 2: secret-as-string broke numeric comparison ───────────────────────────
# Old code did str(secret) on even attempts, so "85" < "9" lexicographically
# would flip the outcome. Fixed code always keeps secret as int.

def test_numeric_compare_not_lexicographic():
    # 85 > 9 numerically → Too High.
    # Lexicographically "85" < "9", which would wrongly return Too Low.
    outcome, _ = check_guess(85, 9)
    assert outcome == "Too High"


def test_two_digit_vs_one_digit_low():
    # 5 < 9 numerically → Too Low.
    outcome, _ = check_guess(5, 9)
    assert outcome == "Too Low"


# ── BUG 3: Hard range was easier than Normal ────────────────────────────────────
# Hard was 1–50, Normal was 1–100. Hard should have a WIDER range.

def test_hard_range_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high   = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


def test_easy_range_is_narrowest():
    _, easy_high   = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high


# ── BUG 4: attempts started at 1, burning first guess ──────────────────────────
# Verified indirectly: attempt 1 should earn near-max points, not be skipped.

def test_first_attempt_win_earns_full_points():
    # attempt_number=1 → 100 - 10*1 = 90 points
    score = update_score(0, "Win", 1)
    assert score == 90


def test_late_attempt_win_earns_minimum_points():
    # attempt_number=10 → 100 - 100 = 0, clamped to 10
    score = update_score(0, "Win", 10)
    assert score == 10


def test_wrong_guess_deducts_points():
    score = update_score(50, "Too High", 1)
    assert score == 45
    score = update_score(50, "Too Low", 1)
    assert score == 45


# ── BUG 5: parse_guess edge cases ──────────────────────────────────────────────

def test_parse_empty_string():
    ok, val, err = parse_guess("")
    assert ok is False
    assert val is None
    assert err is not None


def test_parse_none():
    ok, val, err = parse_guess(None)
    assert ok is False


def test_parse_non_numeric():
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert "number" in err.lower()


def test_parse_float_string_truncates():
    ok, val, err = parse_guess("7.9")
    assert ok is True
    assert val == 7


def test_parse_valid_integer():
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42
    assert err is None

