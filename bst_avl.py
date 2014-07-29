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
        # first left then right
        new_root = self._root._left._right
        new_left = self._root._left
        new_right = self._root
        new_left._right, new_root._left = new_root._left, new_left
        new_right._left, new_root._right = new_root._right, new_right
        self._root = new_root

    def _rotate_rr(self):
        new_root = self._root._right
        new_left = self._root
        new_left._right, new_root._left = new_root._left, new_left
        self._root = new_root

    def _rotate_rl(self):
        # first right then left
        new_root = self._root._right._left
        new_right = self._root._right
        new_left = self._root
        new_left._right, new_root._left = new_root._left, new_left
        new_right._left, new_root._right = new_root._right, new_root._right


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
                elif counter <= 4:
                    insert_location  |= counter
                parent = parent._right
            counter = counter << 1

        # check if there are 2 iterations
        if counter <= 4:
            return
        self._balance -= 1 if insert_location & 1 else : self._balance += 1
        if -2 < self._balance < 2 :
            return
        self._rotations.get(insert_location)
        self._balance = 0

    def _find_node(self, data):
        tmp = self._root
        tmp_parent = None
        while True:
            if val < tmp._data:
                tmp_parent = tmp
                tmp = tmp._left
            elif val > tmp._data:
                tmp_parent = tmp
                tmp = tmp._right
            else:
                return tmp, tmp_parent
            if tmp is None:
                raise IndexError


    def _deletion(self, data):
        if not self._root:
            return
        root_data = self._root._data
        my_node, my_parent = self._find_node(data)
        if my_node._left and my_node._right:
            my_tmp = my_node._right
            if my_tmp._left:
                while my_tmp._left._left:
                    my_tmp = my_tmp._left
                my_node._data = my_tmp._left._data
                if my_tmp._left._right:
                    my_tmp._left = my_tmp._left._right
                else:
                    my_tmp._left = None
            else:
                my_tmp._left = my_node._left
                if self._root == my_node:
                    self._root = my_tmp
                else:
                    my_parent._left = my_tmp
        else:
            del_node = None
            if not my_node._left and not my_node._right:
                del_node = None
            elif not my_node._right:
                del_node = my_node._left
            else:
                del_node = my_node._right
            if my_parent._left == my_node:
                my_parent._left = del_node
            else:
                my_parent._right = del_node

        if data < root_data and self._balance == 1:
            self._rotations.get(0)
            self._balance = 0
        elif data >= root_data and self._balance == -1:
            self._rotations.get(3)
            self._balance = 0




















