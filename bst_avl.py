#!/usr/bin/python

class Node(object):
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

class BST(object):
    def __init__(self):
        self._root = None
        self._balance = 0
        self._rotations = {0:self._rotate_ll(), 1:self._rotate_rl(), 2:self._rotate_lr(), 3:self.rotate_rr()}

    def _rotate_ll(self):
        new_root = self._root._left
        new_right = self._root
        new_right._left, new_root._right = new_root._right, new_right
        self._root = new_root

    def _rotate_lr(self):
        #once left sonra right
        new_root = self._root._left._right
        new_left = self._root._left
        new_right = self._root
        new_left._right, new_root._left = new_root._left, new_left
        new_right._left, new_root._right = new_root._right, new_right
        self._root = new_root

    def _rotate_rr(self):
        new_root = self._root._right
        pass
    def _rotate_rl(self):
        pass

# XY
# 1->right, 0->left

    def _insert(self, data):
        if not self._root:
            self._root = Node(data)
            return
        counter = 1
        insert_location = 0
        parent = self._root
        while True:
            if parent._data == data:
                break
            if data < parent._data:
                if not parent._left:
                    parent._left = Node(data)
                parent = parent._left
            else:
                if not parent._right:
                    parent._right = Node(data)
                parent = parent._right
                if counter < 4:
                    insert_location  |= counter
            counter = counter << 1

        # check if there is 2 iterations
        if counter < 4:
            return
        self._rotations(insert_location)















