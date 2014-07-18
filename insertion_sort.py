#!/usr/bin/python


def insertion_sort(sort_me):
    for i in range(len(sort_me)):
        j = i
        while j-1 >= 0 and sort_me[j] < sort_me[j-1]:
            sort_me[j-1], sort_me[j] = sort_me[j], sort_me[j-1]
            j -= 1
    return sort_me


def time_track(size):
    import time
    a = [size-i for i in xrange(size)]
    print "Worst Case"

    start = time.clock()
    insertion_sort(a)
    end = time.clock()
    print "Insertion Worst: %.2gs" % (end-start)

    a = [i for i in xrange(size)]
    print "Best Case"

    start = time.clock()
    insertion_sort(a)
    end = time.clock()
    print "Insertion Best: %.2gs" % (end-start)


if __name__ == '__main__':
    size = 20000
    print "Size: "+str(size)
    time_track(size)

    sort_me = [5,4,1,13,8,7,2,6,3]
    merge_sort(sort_me, 0, 8)
    for item in sort_me:
        print item,













