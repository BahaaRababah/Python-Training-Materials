from collections import Counter


def filter_evens(numbers):
    return [number for number in numbers if number % 2 == 0]


def get_top_word(word_list):
    counter = Counter(word_list)
    return counter.most_common(1)[0][0]