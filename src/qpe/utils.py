"""Utility functions for the Quantum Poem Engine."""

from typing import List


def extract_pronouns(text: str) -> List[str]:
    """Extract pronouns from text.

    Args:
        text: Input text (poem line or stanza).

    Returns:
        List of pronouns found in the text.
    """
    pronouns = {"she", "he", "it", "they", "them", "her", "his", "their", "i", "you", "we"}
    words = text.lower().split()
    return [word.strip(',.!?;:') for word in words if word.strip(',.!?;:') in pronouns]


def rhyme_check(line1: str, line2: str) -> bool:
    """Check if two lines have matching end sounds (simplified).

    Args:
        line1: First line.
        line2: Second line.

    Returns:
        True if lines appear to rhyme based on last 2 characters.
    """
    word1 = line1.split()[-1].lower().strip(',.!?;:')
    word2 = line2.split()[-1].lower().strip(',.!?;:')
    return word1[-2:] == word2[-2:]


def syllable_count(text: str) -> int:
    """Estimate syllable count in text (simplified).

    Args:
        text: Input text.

    Returns:
        Estimated syllable count.
    """
    vowels = "aeiouy"
    syllable_count_val = 0
    text = text.lower()
    previous_was_vowel = False

    for char in text:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            syllable_count_val += 1
        previous_was_vowel = is_vowel

    # Adjust for silent e
    if text.endswith('e'):
        syllable_count_val -= 1

    return max(1, syllable_count_val)
