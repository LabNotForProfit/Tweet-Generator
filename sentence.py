import sample
import random

# Takes: Histogram | Returns:
def create(length, hist):
    word_start = sample.random_word(hist)
    sentence = next_word(hist, hist[word_start][1], [word_start], length)
    return sentence.capitalize()

#             OG Hist  Consec_hist Sentence      Num Req Words
def next_word(og_hist, word_hist, sentence_list, length):
    rand_index = random.randint(1, len(word_hist))

    if len(sentence_list) == length:
        sentence = " ".join(sentence_list)
        return sentence
    else:
        word = sample.random_word(word_hist)
        if word == "[END]":
            sentence = " ".join(sentence_list)
            return sentence
        sentence_list.append(word)
        return next_word(og_hist, og_hist[word][1], sentence_list, length)
