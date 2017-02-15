import random

# Takes: Histogram | Returns: A Random Word
def random_word(histogram):
    probability = 1
    rand_index = random.randint(1, sum(histogram.values()))
    # Algorithm 2
    for word in histogram:
        probability += histogram[word]
        if probability >= rand_index:
            return word
