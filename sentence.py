import random
import sys
import re

def create(length):
    words = open('./class_1/sample-text.txt', 'r').read()
    word_list = []
    rand_words = []
    sentence = ""

    for word in words.split():
        word = re.sub('[:;-[]', '', word)
        word_list.append(word)

    for _ in range(length):
        rand_index = random.randint(0, len(word_list))

        rand_words.append(word_list[rand_index])

        sentence = " ".join(rand_words)

    return sentence

if __name__ == "__main__":
    dict = open('/Users/alexaaronpena/Github Repositories/Tweet-Generator/class_1/sample-text.txt', 'r')

    word_count = int(sys.argv[1])

    dict_list = []

    rand_words = []

    for word in dict:
        dict_list.append(word.replace('\n', ' '))

    for _ in range(word_count):
        rand_index = random.randint(0, len(dict_list))

        rand_words.append(dict_list[rand_index])

        sentence = "".join(rand_words).replace('\n', ' ')
        print(sentence)
