#!/usr/bin/python


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):
    def __init__(self, data):
        self.head = Node(data)

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        try:
            head_val, self.head = self.head.data, self.head.next
            return head_val
        except AttributeError:
            raise AttributeError(u"Nothing to delete")
