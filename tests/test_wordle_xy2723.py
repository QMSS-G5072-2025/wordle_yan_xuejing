from wordle_xy2723.wordle_xy2723 import validate_guess, check_guess

def test_validate_guess():
    """
    Test the validate_guess function with various inputs.
    
    TODO: Students should implement this test function with:
    - Valid guesses (correct length, lowercase, alphabetic)
    - Invalid guesses (wrong length, uppercase, non-alphabetic)
    - Edge cases (empty string, None, non-string inputs)
    """
    # The word must be 5 character
    assert validate_guess("apple") == True # correct length
    assert validate_guess("app") == False # wrong length, too short
    assert validate_guess("apples") == False # wrong length, too long

    # The word must be lowercase
    assert validate_guess("apple") == True # lowercase
    assert validate_guess("APPLE") == False # uppercase
    assert validate_guess("Apple") == False # mixed

    # The word must be alphabetic
    assert validate_guess("APP1E") == False # non-alphabetic
    assert validate_guess("Apple!") == False # non-alphabetic

    assert validate_guess("") == False # empty string
    assert validate_guess(None) == False # None
    assert validate_guess(1234) == False # non-string inputs


def test_check_guess_basic():
    """
    Test basic check_guess functionality.
    
    TODO: Students should implement this test function with:
    - Perfect match (all green)
    - No matches (all gray)
    - Mixed results (green, yellow, gray combinations)
    - Edge cases (different lengths)
    
    Remember: Run check_guess() with different inputs first to see what it returns!
    """
    # Perfect match (all green)
    result = check_guess("crane", "crane")
    expected = [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]
    assert result == expected

    # No matches (all gray)
    result = check_guess("crane", "swift")
    expected = [('s', 'gray'), ('w', 'gray'), ('i', 'gray'), ('f', 'gray'), ('t', 'gray')]
    assert result == expected

    # Mixed results (green, yellow, gray combinations)
    result = check_guess("crane", "cones")
    expected = [('c', 'green'), ('o', 'gray'), ('n', 'yellow'), ('e', 'yellow'), ('s', 'gray')]
    assert result == expected

    # Edge cases (different lengths)
    result = check_guess("crane", "content")
    expected = []
    assert result == expected

    # Mixed case
    result = check_guess("crane", "Crane")
    expected = [('C', 'gray'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]
    assert result == expected