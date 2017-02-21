import random

# Takes: Histogram | Returns: A Random Word
def random_word(histogram):
    # Using Algorithm 2 (less code)
    probability = 0
    rand_index = 0

    # Handles getting truly random word from all words in source text histogram
    if hasattr(histogram, 'tokens'):
        rand_index = random.randint(1, histogram.tokens)
        for word in histogram:
            probability += histogram[word][0]
            if probability >= rand_index:
                return word

    # Handles getting truly random word from consecutive words histogram
    else:
        rand_index = random.randint(1, sum(histogram.values()))
        for word in histogram:
            probability += histogram[word]
            if probability >= rand_index:
                return word
