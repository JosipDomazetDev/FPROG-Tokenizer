import re
from functools import reduce
from typing import List, Dict, Tuple

# Step 2: Read files
read_file = lambda filename: [line.strip() for line in open(filename, 'r')]

# Step 3: Tokenize the text
tokenize = lambda text: re.findall(r'\b\w+\b', text.lower())

# Step 4: Filter words
filter_words = lambda words, filter_list: list(
    filter(lambda current_filter_word: current_filter_word in words, filter_list))

# Step 5: Count occurrences
count_occurrences = lambda words: reduce(lambda acc, word: {**acc, **{word: acc.get(word, 0) + 1}}, words, {})


# Step 6: Calculate term density
def calculate_density(occurrences: Dict[str, int], total_words: int) -> float:
    return sum(occurrences.values()) / total_words


# Step 7: Read input files and tokenize
book_content = read_file('./res/war_and_peace.txt')
war_terms = set(tokenize(' '.join(read_file('./res/war_terms.txt'))))
peace_terms = set(tokenize(' '.join(read_file('./res/peace_terms.txt'))))


# Step 8: Process chapters
def process_chapters(chapters: List[str], war_terms, peace_terms) -> List[Tuple[float, float]]:
    return list(map(lambda chapter: (
        calculate_density(count_occurrences(filter_words(tokenize(chapter), war_terms)), len(tokenize(chapter))),
        calculate_density(count_occurrences(filter_words(tokenize(chapter), peace_terms)), len(tokenize(chapter)))
    ), chapters))


