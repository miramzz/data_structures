#!/usr/bin/python


def insertion_sort(sort_me):
    for i in range(len(sort_me)):
        j = i
        while j-1 >= 0 and sort_me[j] < sort_me[j-1]:
            sort_me[j-1], sort_me[j] = sort_me[j], sort_me[j-1]
            j -= 1
    #return sort_me

def time_track(size):
    import time
    a = [size-i for i in xrange(size)]
    print "Worst Case"

    a = [i for i in xrange(size)]
    print "Best Case"

    start = time.clock()
    insertion_sort(a)
    end = time.clock()
    print "Insertion: %.2gs" % (end-start)


if __name__ == '__main__':
    size = 20000
    print "Size: "+str(size)
    time_track(size)