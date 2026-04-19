import pytest
from string_utils import *

# count_vowels
def test_count_vowels_normal():
    assert count_vowels("hello") == 2

def test_count_vowels_uppercase():
    assert count_vowels("AEIOU") == 5

def test_count_vowels_empty():
    assert count_vowels("") == 0


# reverse_string
def test_reverse_string_basic():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single():
    assert reverse_string("a") == "a"

def test_reverse_string_empty():
    assert reverse_string("") == ""


# is_palindrome
def test_palindrome_simple():
    assert is_palindrome("racecar") is True

def test_palindrome_sentence():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_palindrome_false():
    assert is_palindrome("hello") is False


# word_count
def test_word_count_basic():
    assert word_count("Hello World") == 2

def test_word_count_spaces():
    assert word_count("   hello   ") == 1

def test_word_count_empty():
    assert word_count("") == 0


# capitalise_words
def test_capitalise_words_basic():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_words_mixed():
    assert capitalise_words("hELLo woRLd") == "Hello World"

def test_capitalise_words_empty():
    assert capitalise_words("") == ""


# remove_duplicates
def test_remove_duplicates_basic():
    assert remove_duplicates("aaabbb") == "ab"

def test_remove_duplicates_mixed():
    assert remove_duplicates("aabbccaa") == "abca"

def test_remove_duplicates_single():
    assert remove_duplicates("a") == "a"


# Exception test (IMPORTANT for marks)
def test_none_input_raises_error():
    with pytest.raises(TypeError):
        count_vowels(None)

# Test None for all functions
def test_reverse_string_none():
    with pytest.raises(TypeError):
        reverse_string(None)

def test_is_palindrome_none():
    with pytest.raises(TypeError):
        is_palindrome(None)

def test_word_count_none():
    with pytest.raises(TypeError):
        word_count(None)

def test_capitalise_words_none():
    with pytest.raises(TypeError):
        capitalise_words(None)

def test_remove_duplicates_none():
    with pytest.raises(TypeError):
        remove_duplicates(None)


# Edge cases
def test_is_palindrome_empty():
    assert is_palindrome("") is True

def test_remove_duplicates_empty():
    assert remove_duplicates("") == ""