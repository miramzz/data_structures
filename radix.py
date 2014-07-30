



def radix_sort(sort_me):
    new_list = []
    index = 0
    all_finished = False
    len_ = len(sort_me)
    while True:
        if all_finished:
            break
        bucket_list = [-1 for i in xrange(127)]
        for item in sort_me:
            if isinstance(item, int):
                str_item = str(item)
                try:
                    ch_ = str_item[len(str_item)-index-1]
                    all_finished = False
                except IndexError:
                    new_list.append(item)
                    all_finished = True
                    continue
            else :
                try:
                    ch_ = item[index]
                    all_finished = False
                except IndexError:
                    new_list.append(item)
                    all_finished = True
                    continue
            tmp = ord(ch_)
            if bucket_list[tmp] == -1:
                bucket_list[tmp] = []
            bucket_list[tmp].append(item)
        for item in bucket_list:
            if item == -1:
                continue
            sort_me += item
        del sort_me[0:len_]
        index +=1

    new_list += sort_me
    return new_list



def time_track(size):
    import time
    a = [size-i for i in xrange(size)]
    print "Worst Case"

    start = time.clock()
    radix_sort(a)
    end = time.clock()
    print "radix Worst: %.2gs" % (end-start)

    a = [i for i in xrange(size)]
    print "Best Case"

    start = time.clock()
    radix_sort(a)
    end = time.clock()
    print "radix Best: %.2gs" % (end-start)


if __name__ == '__main__':
    # size = 2000
    # print "Size: "+str(size)
    # time_track(size)

    sort_me = [5,4,1,13,8,7,2,3,6]
    new_list = radix_sort(sort_me)
    print "NEW LIST"
    for item in new_list:
        print item,

    print
    unsort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    unsort_repeated = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9]
    sorted_repeated = [9, 9, 9, 9, 9, 10, 10, 10, 10, 10]

    unsort = radix_sort(unsort)
    unsort_repeated = radix_sort(unsort_repeated)
    print unsort == sort
    print unsort_repeated == sorted_repeated
