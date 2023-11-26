import re
from typing import List, Dict, Tuple


# Step 2: Read files
def read_file(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


# Step 3: Tokenize the text
tokenize = lambda text: re.findall(r'\b\w+\b', text)

# Step 4: Filter words
filter_words = lambda words, filter_list: list(
    filter(lambda current_filter_word: current_filter_word in words, filter_list))

# Step 5: Count occurrences
count_occurrences = lambda text_words, words_to_be_counted: {word: text_words.count(word) for word in
                                                             words_to_be_counted}


# Step 6: Calculate term density
def calculate_density(occurrences: Dict[str, int], total_words: int) -> float:
    if total_words == 0:
        return 0

    return sum(occurrences.values()) / total_words


# Step 8: Process chapters
def process_chapters(chapters: List[str], war_terms, peace_terms) -> List[Tuple[float, float]]:
    results = []

    for chapter in chapters:
        tokenized_chapter = tokenize(chapter)

        war_density = calculate_density(
            count_occurrences(tokenized_chapter, filter_words(tokenized_chapter, war_terms)), len(tokenized_chapter))
        peace_density = calculate_density(
            count_occurrences(tokenized_chapter, filter_words(tokenized_chapter, peace_terms)), len(tokenized_chapter))
        results.append((war_density, peace_density))

    return results


# Step 9: Categorize chapters
def categorize_chapters(density_tuples):
    return ['war' if war > peace else 'peace' for war, peace in density_tuples]


# Step 10: Get print results
get_print_results = lambda chapter_densities: [f"Chapter {i + 1}: {categorized_chapter}-related" for
                                               i, categorized_chapter in
                                               enumerate(categorize_chapters(chapter_densities))]


def get_tolstoy_lines():
    # Step 7: Read input files and tokenize
    book_content = read_file('./res/war_and_peace.txt')
    war_terms = set(tokenize(' '.join(read_file('./res/war_terms.txt'))))
    peace_terms = set(tokenize(' '.join(read_file('./res/peace_terms.txt'))))

    # Extract chapters from the book
    chapters = re.split(r'\bchapter\b \d+', ' '.join(book_content), flags=re.IGNORECASE)[1:]
    chapter_densities = process_chapters(chapters, war_terms, peace_terms)

    return get_print_results(chapter_densities)


# Step 10b: Print results
if __name__ == '__main__':
    for line in get_tolstoy_lines():
        print(line)

    # categorized_chapters = categorize_chapters(chapter_densities)
    # for i, category in enumerate(categorized_chapters):
    #     print(f"Chapter {i + 1}: {category}-related")
