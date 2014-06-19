#!/usr/bin/python
import stack
import pytest


def test_init():
    try:
        stack.Stack()
    except TypeError:
        print u"Passed init test"
    s = stack.Stack(4)
    assert s.head.data == 4


def test_push():
    s = stack.Stack(7)
    s.push(5)
    assert s.head.next.data == 7
    assert s.head.data == 5

    s.pop()
    s.pop()
    s.push(4)
    assert s.head.data == 4
    print u'Passed insert test'


def test_pop():
    s = stack.Stack(5)
    s.push(7)
    assert s.pop() == 7
    assert s.head.data == 5
    assert s.pop() == 5
    with pytest.raises(AttributeError):
        assert s.pop() is None
    print u'Passed pop test'
