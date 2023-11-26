import unittest
from main import *


class TestCase(unittest.TestCase):
    def test_tokenize(self):
        text = "this  is a test sentence."
        tokens = tokenize(text)
        self.assertEqual(tokens, ["this", "is", "a", "test", "sentence"])

    def test_filter_words(self):
        words = ["apple", "banana", "cherry", "banana", "date"]
        filter_list = ["banana", "date"]
        filtered_words = filter_words(words, filter_list)
        self.assertEqual(filtered_words, ["banana", "date"])

    def test_count_occurrences(self):
        words = ["apple", "banana", "cherry", "banana", "date"]
        words_to_be_counted = ["banana", "date"]

        occurrences = count_occurrences(words, words_to_be_counted)
        self.assertEqual(occurrences, {"banana": 2, "date": 1})

    def test_calculate_density(self):
        word_occurrences = {"apple": 2, "banana": 3, "cherry": 1}
        total_words = 10

        expected_density = 0.6  # (2 + 3 + 1) / 10

        density = calculate_density(word_occurrences, total_words)

        assert density == expected_density, f"Expected {expected_density}, but got {density}"

    def test_process_chapters(self):
        chapters = ["this is a test chapter.", "another test chapter.", "yet another chapter."]
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

    def test_chapter2(self):
        book_content = re.split(r'\bchapter\b \d+', ' '.join(read_file('chapter2.txt')))[-1]
        book_content_tokenized = tokenize(book_content)

        war_terms = set(tokenize(' '.join(read_file('../res/war_terms.txt'))))
        peace_terms = set(tokenize(' '.join(read_file('../res/peace_terms.txt'))))

        count_occurrences_war = count_occurrences(book_content_tokenized,
                                                  filter_words(book_content_tokenized, war_terms))
        count_occurrences_peace = count_occurrences(book_content_tokenized,
                                                    filter_words(book_content_tokenized, peace_terms))

        self.assertEqual(count_occurrences_war, {'afraid': 1, 'fear': 1, 'general': 1, 'war': 1})
        self.assertEqual(count_occurrences_peace, {'smile': 3, 'peace': 1})

    def test_chapter8(self):
        book_chapters = re.split(r'\bchapter\b \d+', ' '.join(read_file('chapter8.txt')))
        book_content_tokenized = tokenize(book_chapters[-1])

        war_terms = set(tokenize(' '.join(read_file('../res/war_terms.txt'))))
        peace_terms = set(tokenize(' '.join(read_file('../res/peace_terms.txt'))))

        count_occurrences_war = count_occurrences(book_content_tokenized,
                                                  filter_words(book_content_tokenized, war_terms))
        count_occurrences_peace = count_occurrences(book_content_tokenized,
                                                    filter_words(book_content_tokenized, peace_terms))

        self.assertEqual(count_occurrences_war, {'general': 1, 'war': 2})
        self.assertEqual(count_occurrences_peace, {'calm': 1, 'freedom': 1, 'love': 1, 'smile': 2, 'supper': 2})

        expected = [(0.0024311183144246355, 0.005672609400324149)]
        result = process_chapters(book_chapters, war_terms, peace_terms)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
