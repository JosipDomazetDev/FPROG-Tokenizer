from functools import reduce
from typing import List, Dict, Tuple
import re

# Step 2: Read files
read_file = lambda filename: [line.strip() for line in open(filename, 'r')]

# Step 3: Tokenize the text
tokenize = lambda text: re.findall(r'\b\w+\b', text.lower())

# Step 4: Filter words
filter_words = lambda words, filter_list: list(
    filter(lambda current_filter_word: current_filter_word in words, filter_list))

# Step 5: Count occurrences
count_occurrences = lambda words: reduce(lambda acc, word: {**acc, **{word: acc.get(word, 0) + 1}}, words, {})

