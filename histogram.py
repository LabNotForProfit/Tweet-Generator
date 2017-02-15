# Takes: Clean List of words | Returns: Updated Histogram
class Histogram(dict):

    def __init__(self, iterable=None):
        super(Histogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        for item in iterable:
            if item in self:
                self[item] += 1
            else:
                self[item] = 1

    def count(self, item):
        return self.get(item, 0)
