#from challenges.01_score_even_vowels import get_words_score
from challenges.score_even_vowels import get_words_score

def test_01_get_words_score():
    assert get_words_score("hacker book") == 4
