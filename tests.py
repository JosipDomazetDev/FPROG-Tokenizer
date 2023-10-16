import unittest
from main import *


class TestCase(unittest.TestCase):
    def test_tokenize(self):
        text = "This is a test sentence."
        tokens = tokenize(text)
        self.assertEqual(tokens, ["this", "is", "a", "test", "sentence"])

    def test_filter_words(self):
        words = ["apple", "banana", "cherry", "banana", "date"]
        filter_list = ["banana", "date"]
        filtered_words = filter_words(words, filter_list)
        self.assertEqual(filtered_words, ["banana", "date"])

    def test_count_occurrences(self):
        words = ["apple", "banana", "cherry", "banana", "date"]
        occurrences = count_occurrences(words)
        self.assertEqual(occurrences, {"apple": 1, "banana": 2, "cherry": 1, "date": 1})

if __name__ == '__main__':
    unittest.main()
