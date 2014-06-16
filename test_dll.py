#!/usr/bin/python


import dll


def test_string():
    l = dll.doublyll(7)
    assert str(l) == "(7)"

def test_init():
    try :
        x = dll.doublyll()
    except TypeError :
        print u"Passed init test"

def test_insert():
    l = dll.doublyll(7)
    l.insert(5)
    assert str(l) == "(5, 7)"
    assert l.head.getdata() == 5
    assert l.tail.getdata() == 7
    assert l.head.next == l.tail
    assert l.tail.prev == l.head

    l.pop()
    l.pop()
    l.insert(3)
    assert str(l) == "(3)"
    assert l.head.getdata() == 3
    assert l.head == l.tail

    print u'Insert tests passed'

def test_pop():
    l = dll.doublyll(7)
    l.insert(5)

    assert l.pop() == 5
    assert l.head == l.tail
    assert l.head.getdata() == 7
    assert l.pop() == 7
    assert l.pop() == None
    print u"Pop method tests passed"

def test_shift():
    l = dll.doublyll(7)
    l.shift()
    assert l.head == l.tail
    assert l._size == 0

    l.insert(3)
    l.insert(7)
    l.shift()
    assert l.head.getdata() == 7
    assert l.tail == l.head
    assert l._size == 1

def test_remove():
    l = dll.doublyll(7)
    l.insert(5)
    l.insert(8)
    l.insert(3)

    l.remove(8)
    assert str(l) == "(3, 5, 7)"

    l.remove(7)
    assert l.tail.getdata() == 5

    l.remove(3)
    assert l.head == l.tail
    assert l.head.getdata() == 5

    print u'Passed remove test'

