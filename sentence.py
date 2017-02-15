import sample
# Takes: Histogram | Returns:
def create(length, dict):
    word_list = []
    sentence = ""

    for _ in range(length):
        word = sample.random_word(dict)
        word_list.append(word)

    sentence = " ".join(word_list)

    return sentence
