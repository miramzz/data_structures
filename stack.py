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
            head_val = self.head.data
            self.head = self.head.next
            return head_val
        except AttributeError:
            pass

    def print_(self):
        tmp_node = self.head
        while tmp_node:
            print tmp_node.data
            tmp_node = tmp_node.next
        else:
            return
        print u"Stack is Empty"

if __name__ == '__main__':

    test = Stack(5)
    test.push(6)
    test.pop()
    test.pop()

    test2 = Stack(3)
    test2.print_()
    test2.pop()
    test2.print_()
    test2.push(4)
    test2.print_()
    test2.pop()
    test2.print_()
