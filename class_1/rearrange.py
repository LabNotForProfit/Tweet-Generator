import random
import sys

text = sys.argv
del text[0]

def random_words():
    for index, word in enumerate(text):
        rand_index_1 = random.randint(0, len(text) - 1)

        tmp = text[index]
        text[index] = text[rand_index_1]
        text[rand_index_1] = tmp

    return text

print(random_words())
