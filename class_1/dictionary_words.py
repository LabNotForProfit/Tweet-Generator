import random
import sys
import linecache

dict = open('/usr/share/dict/words', 'r')

# dict_list = []
#
# rand_words = []
#
# for word in dict:
#     dict_list.append(word.replace('\n', ' '))
#
# for _ in range(word_count):
#     rand_index = random.randint(0, 235886)
#
#     rand_words.append(dict_list[rand_index])
#
# print rand_words

word_count = int(sys.argv[1])

rand_words = []

for _ in range(word_count):
    rand_index = random.randint(1, 235886)

    rand_words.append(linecache.getline('/usr/share/dict/words', rand_index))

sentence = "".join(rand_words).replace('\n', ' ')
print(sentence)
