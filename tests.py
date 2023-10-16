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

    def test_calculate_density(self):
        word_occurrences = {"apple": 2, "banana": 3, "cherry": 1}
        total_words = 10

        expected_density = 0.6  # (2 + 3 + 1) / 10

        density = calculate_density(word_occurrences, total_words)

        assert density == expected_density, f"Expected {expected_density}, but got {density}"

    def test_process_chapters(self):
        chapters = ["This is a test chapter.", "Another test chapter.", "Yet another chapter."]
        war_terms = {"test"}
        peace_terms = {"another"}

        expected_results = [
            (0.2, 0.0),
            (0.3333333333333333, 0.3333333333333333),
            (0.0, 0.3333333333333333)
        ]

        results = process_chapters(chapters, war_terms, peace_terms)

        assert results == expected_results, f"Expected {expected_results}, but got {results}"

    def test_categorize_chapters(self):
        densities = [(0.25, 0.25), (0.4, 0.3), (0.2, 0.5), (0.5, 0.5)]
        expected_results = ["peace", "war", "peace", "peace"]

        results = categorize_chapters(densities)

        assert results == expected_results, f"Expected {expected_results}, but got {results}"

    def test_get_print_results(self):
        densities = [(0.25, 0.25), (0.4, 0.3), (0.2, 0.5), (0.5, 0.5)]
        expected_results = ['Chapter 1: peace-related', 'Chapter 2: war-related', 'Chapter 3: peace-related',
                            'Chapter 4: peace-related']

        results = get_print_results(densities)

        assert results == expected_results, f"Expected {expected_results}, but got {results}"

    def test_complete(self):
        tolstoy_lines = get_tolstoy_lines()
        output_lines = read_file("./res/output.txt")

        self.assertTrue(len(tolstoy_lines), len(output_lines))

        print(len(tolstoy_lines))
        print(len(output_lines))

        for line1, line2 in zip(tolstoy_lines, output_lines):
            assert line1 == line2, f"Expected line: {line1}, but got: {line2}"


if __name__ == '__main__':
    unittest.main()
