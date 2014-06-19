#!/usr/bin/python


import stack


def test_string():
    s = stack.Stack(7)
    assert str(s) == "(7)"


def test_insert():
    s = stack.Stack(7)
    s.insert(5)
    assert str(s) == "(5, 7)"

    s.pop()
    s.pop()
    s.push(4)
    assert str(s) == "(4)"
    print u'Passed insert test'


def test_pop():
    s = stack.Stack(5)
    assert s.pop() == 5
    assert s.pop() is None
    print u'Passed pop test'
