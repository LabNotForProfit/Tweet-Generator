# Takes: Clean List of words | Returns: Updated Histogram
class Histogram(dict):
    # Key: (tokens_of_word, histogram_of_consecutive_words)

    def __init__(self, iterable=None):
        super(Histogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        for index, item in enumerate(iterable):
            if item in self:
                updated_tup = self[item]
                consec_items_hist = updated_tup[1]

                if index + 1 < len(iterable):
                    item_right = iterable[index + 1]
                    if item_right in consec_items_hist:
                        consec_items_hist[item_right] += 1
                    else:
                        consec_items_hist[item_right] = 1

                self.tokens += 1
                self[item] = (updated_tup[0] + 1, consec_items_hist)
            else:
                consec_items_hist = {}

                # If there is a word to the right of current word
                if index + 1 < len(iterable):
                    item_right = iterable[index + 1]
                    consec_items_hist[item_right] = 1
                # Else this is the last word in all of our text
                else:
                    consec_items_hist["[END]"] = 1

                self.types += 1
                self.tokens += 1
                self[item] = (1, consec_items_hist)


    def count(self, item):
        return self.get(item, 0)[0]
