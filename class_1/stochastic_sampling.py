import sys
import re
import random

def histogram(source_text):
    histogram = {}
    for word in source_text.split():
        word = re.sub('[.,:;!-[]?', '', word)

        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram.get(word, 0)

def random_word(histogram):
    probability = 1
    rand_index = random.randint(1, sum(histogram.values()))
    for (key, value) in histogram.items():
        for num in range(1, value + 1):
            if probability == rand_index:
                if key in outcome_gram:
                    outcome_gram[key] += 1
                else:
                    outcome_gram[key] = 1
                return outcome_gram
            else:
                probability += 1

if __name__ == "__main__":
    outcome_gram = {}
    dict = open('/Users/alexaaronpena/Github Repositories/Tweet-Generator/class_1/fish.txt', 'r')
    text = dict.read()
    dict.close()

    # print(histogram(text))
    # print(unique_words(histogram(text)))
    # print(frequency("alex", histogram(text)))
    for number in range(1, 10000):
        random_word(histogram(text))

    # print("If this were a perfect algorithm, the number of fish would be 5000, but my actual value is " + str(outcome_gram["fish"]))
    # print("The percent error is " + str(abs(outcome_gram["fish"] - 5000.0) / 5000.0 * 100.0) + "%")
    # outcome_gram["fish"] = abs(outcome_gram["fish"] - 5000.0) / 5000.0 * 100.0
