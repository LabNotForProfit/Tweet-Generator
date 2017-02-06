import sys
import re

def histogram(source_text):
    histogram = {}
    for word in source_text.split():
        word = re.sub('[.,:]', '', word)

        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram.get(word, 0)

if __name__ == "__main__":
    dict = open('/Users/alexaaronpena/Github Repositories/Tweet-Generator/class_1/sample-text.txt', 'r')
    text = dict.read()
    dict.close()

    # print(histogram(text))
    # print(unique_words(histogram(text)))
    print(frequency("alex", histogram(text)))
