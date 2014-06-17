#!/usr/bin/python


class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def getdata(self):
        return self.value


class doublyll(object):
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self._size = 1

    def insert(self, value):
        if self._is_empty():
            self.__init__(value)
            return
        new_node = Node(value, next=self.head)
        self.head.prev, self.head = new_node, new_node
        if self._size == 1:
            self.tail.prev = self.head
        self._size += 1

    def _is_empty(self):
        if not self.head:
            print u"Link is empty"
            return True
        return False

    def pop(self):
        if self._is_empty():
            return
        elif self._size == 1:
            val = self.head.value
            self.head = self.tail = None
            self._size = 0
            return val
        else:
            val, self.head = self.head.value, self.head.next
            self._size -= 1
        return val

    def shift(self):
        if self._is_empty():
            return
        elif self._size == 1:
            return self.pop()
        else:
            self.tail.prev.next, self.tail = self.tail.next, self.tail.prev
            self._size -= 1

    def _findNode(self, val):
        tmp_node = self.head
        while not tmp_node.next:
            if tmp_node.getdata() == val:
                return tmp_node
            tmp_node = tmp_node.next
        else:
            raise IndexError

    def remove(self, val):
        if self._is_empty():
            return
        vnode = self._findNode(val)
        print vnode
        if vnode == self.head:
            return self.pop()
        elif vnode == self.tail:
            return self.shift()
        else:
            print vnode.getdata()
            vnode.prev.next, vnode.next.prev = vnode.next, vnode.prev
        self._size -= 1

    def __str__(self):
        tmp_node = self.head
        str_ = "("
        while tmp_node:
            str_ += str(tmp_node.value) + ", "
            tmp_node = tmp_node.next
        return str_[:-2]+")" if len(str_) > 1 else str_+")"
