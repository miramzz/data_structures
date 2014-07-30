
def randSelection(f_index, l_index):
    import random
    return random.randint(f_index, l_index-1)

def quick_partition(sort_me, f_index, l_index):
    p_index = randSelection(f_index, l_index)
    sort_me[f_index], sort_me[p_index] = sort_me[p_index], sort_me[f_index]

    p_index = f_index+1
    while (p_index < l_index) and (sort_me[p_index] < sort_me[f_index]):
        p_index += 1

    index = l_index-1
    while index >= p_index:
        if sort_me[f_index] > sort_me[index]:
            sort_me[index], sort_me[p_index] = sort_me[p_index], sort_me[index]
            p_index += 1
            index += 1
        index -= 1
    sort_me[f_index], sort_me[p_index-1] = sort_me[p_index-1], sort_me[f_index]
    return p_index-1

def quick_sort(sort_me, f_index, l_index):
    if f_index < l_index-1:
        pivot = quick_partition(sort_me, f_index, l_index)
        quick_sort(sort_me, f_index, pivot)
        quick_sort(sort_me, pivot+1, l_index)


def time_track(size):
    import time
    a = [size-i for i in xrange(size)]
    print "Worst Case"

    start = time.clock()
    quick_sort(a, 0, size-1)
    end = time.clock()
    print "quick Worst: %.2gs" % (end-start)

    a = [i for i in xrange(size)]
    print "Best Case"

    start = time.clock()
    quick_sort(a, 0, size-1)
    end = time.clock()
    print "quick Best: %.2gs" % (end-start)


if __name__ == '__main__':
    size = 2000
    print "Size: "+str(size)
    time_track(size)

    sort_me = [5,4,1,13,8,7,2,6,3]
    quick_sort(sort_me, 0, 9)
    for item in sort_me:
        print item,

    print
    unsort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    unsort_repeated = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9]
    sorted_repeated = [9, 9, 9, 9, 9, 10, 10, 10, 10, 10]

    quick_sort(unsort, 0, 10)
    quick_sort(unsort_repeated, 0, 10)
    print unsort == sort
    print unsort_repeated == sorted_repeated
