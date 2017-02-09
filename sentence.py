import random
import sys
import re

def create(length, dict):
    word_list = []
    sentence = ""

    for _ in range(length):
        word = random_word(dict)
        word_list.append(word)

    sentence = " ".join(word_list)

    return sentence

def open_file():
    dict = open('./class_1/sample-text.txt', 'r')
    hist_dict = histogram(dict.read())
    dict.close()

    return hist_dict

# Creates a histogram from a source text
def histogram(source_text):
    histogram = {}
    for word in source_text.split():
        word = re.sub('[.,:;!-[]?', '', word)

        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram

def random_word(histogram):
    probability = 1
    rand_index = random.randint(1, sum(histogram.values()))
    # Algorithm 2
    for word in histogram:
        probability += histogram[word]
        if probability >= rand_index:
            return word
