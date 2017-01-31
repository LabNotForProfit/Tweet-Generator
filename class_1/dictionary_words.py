import random
import sys

dict = open('/usr/share/dict/words', 'r')

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
