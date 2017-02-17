import sys
import random

# Takes: Clean List of words | Returns: Updated Histogram
class Histogram(dict):

    def __init__(self, source_text_list=None):
        super(Histogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if source_text_list:
            self.update(source_text_list)

    def update(self, source_text_list):
        for index, word in enumerate(source_text_list):

            if word in self:
                prev_tup = self[word]
                word_histogram = prev_tup[1]

                if index + 1 < len(source_text_list):
                    word_right = source_text_list[index + 1]

                    if word_right in word_histogram:
                        word_histogram[word_right] += 1
                    else:
                        word_histogram[word_right] = 1

                self.tokens += 1
                self[word] = (prev_tup[0] + 1, word_histogram)
            else:
                word_histogram = {}

                if index + 1 < len(source_text_list):
                    word_right = source_text_list[index + 1]
                    word_histogram[word_right] = 1
                self.types += 1
                self.tokens += 1
                self[word] = (1, word_histogram)

    def count(self, item):
        return self.get(item, 0)[0]

def tokenize(source_text):
    return source_text.split()

def random_word(histogram):
    probability = 0
    rand_index = 0
    if hasattr(histogram, 'tokens'):
        print("tokens")
        rand_index = random.randint(1, histogram.tokens)

        # Algorithm 2
        for word in histogram:
            probability += histogram[word][0]
            if probability >= rand_index:
                return word
    else:
        rand_index = random.randint(1, sum(histogram.values()))

        # Algorithm 2
        for word in histogram:
            probability += histogram[word]
            if probability >= rand_index:
                return word
    # return histogram

def sentence(histogram, word_count):
    word_start = random_word(histogram)

    sentence = next_word(histogram, histogram[word_start][1], [word_start], word_count)
    return sentence


def next_word(og_hist, word_hist, sentence_list, word_count):
    rand_index = random.randint(1, len(word_hist))

    if len(sentence_list) == word_count:
        sentence = " ".join(sentence_list)
        return sentence
    else:
        word = random_word(word_hist)
        sentence_list.append(word)
        return next_word(og_hist, og_hist[word][1], sentence_list, word_count)


if __name__ == "__main__":
    # outcome_gram = {}
    dict = open('/Users/alexaaronpena/Github Repositories/Tweet-Generator/text_files/fish.txt', 'r')
    text = dict.read()
    dict.close()

    tokens = tokenize(text)
    hist_dict = Histogram(tokens)

    # print(sentence(hist_dict, 5))
    print(hist_dict)
    print(sentence(hist_dict, 5))
