#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of items
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # TODO: append given item
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # TODO: prepend given item
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        item_match = None
        previous = None
        current = self.head
        while current is not None:
            if current.data == item:
                item_match = current
                break
            previous = current
            current = current.next

        if item_match is not None:
            if previous is not None:
                if item_match is self.tail:
                    previous.next = item_match.next
                    self.tail = previous
                else:
                    # print(previous.next)
                    previous.next = item_match.next
                    # print(previous.next)
            else:
                if item_match.next is not None:
                    self.head = self.head.next
                else:
                    self.head = None
                    self.tail = None
        else:
            raise ValueError

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        current = self.head
        while current is not None:
            if quality(current.data):
                return current.data
            current = current.next
        return None


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))

    # Enable this after implementing delete:
    # print('Deleting items:')
    # ll.delete('B')
    # print(ll)
    # ll.delete('C')
    # print(ll)
    # ll.delete('A')
    # print(ll)
    # print('head: ' + str(ll.head))
    # print('tail: ' + str(ll.tail))
    # print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()
