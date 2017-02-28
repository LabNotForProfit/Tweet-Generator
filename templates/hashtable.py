#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    # O(1)
    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    # O(n^2)
    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    # O(n)
    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets
        bucket_values = []
        for bucket in self.buckets:
            bucket_values += [val[1] for val in bucket.items()]
        return bucket_values

    # O(n)
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    # O(n)
    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # TODO: Count number of key-value entries in each of the buckets
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count

    # O(n)
    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket
        bucket_index = hash(key) % len(self.buckets) # Hashes key and maps it to value in bucket range
        bucket = self.buckets[bucket_index]
        searched_item = bucket.find(lambda item: item[0] == key)
        if searched_item is not None:
            return True
        return False

    # O(n)
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        # Hashes key and maps it to value in bucket range
        bucket_index = hash(key) % len(self.buckets) # O(1)
        bucket = self.buckets[bucket_index] # O(1)
        searched_item = bucket.find(lambda item: item[0] == key) # O(n)
        if searched_item is not None:
            return searched_item[1]
        raise KeyError

    # O(n)
    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket
        bucket_index = hash(key) % len(self.buckets) # Hashes key and maps it to value in bucket range
        bucket = self.buckets[bucket_index]
        new_item = (key, value)
        searched_item = bucket.find(lambda item: item[0] == key)
        if searched_item is not None:
            # Update existing value
            self.buckets[bucket_index].delete(key)
            self.buckets[bucket_index].append(new_item)
            pass
        else:
            bucket.append(new_item) # Set new value

    # O(n)
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found
        bucket_index = hash(key) % len(self.buckets) # Hashes key and maps it to value in bucket range
        try:
            self.buckets[bucket_index].delete(key)
        except ValueError:
            raise KeyError

def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))
    print('Updating entries:')
    ht.set('I', 5)
    print(ht)
    ht.set('V', 1)
    print(ht)

    # Enable this after implementing delete:
    print('Deleting entries:')
    ht.delete('I')
    print(ht)
    ht.delete('V')
    print(ht)
    ht.delete('X')
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
