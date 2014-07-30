

def merge(sort_me, f_index, m_index, l_index):
    tmp_index = m_index-1
    while m_index >= f_index:
        if sort_me[m_index]>sort_me[m_index+1]:
            sort_me[m_index], sort_me[m_index+1] = sort_me[m_index+1], sort_me[m_index]
            m_index += 1
            if m_index != l_index:
                continue
        m_index = tmp_index
        tmp_index -= 1

def merge_sort(sort_me, f_index, l_index):
    diff_index = l_index - f_index
    if diff_index > 1:
        m_index = (f_index+l_index)//2
        merge_sort(sort_me, f_index, m_index)
        merge_sort(sort_me, m_index+1, l_index)
        merge(sort_me, f_index, m_index, l_index)
    elif sort_me[f_index]>sort_me[l_index]:
        sort_me[f_index], sort_me[l_index] = sort_me[l_index], sort_me[f_index]
    return sort_me

def time_track(size):
    import time
    a = [size-i for i in xrange(size)]
    print "Worst Case"

    start = time.clock()
    merge_sort(a, 0, size-1)
    end = time.clock()
    print "Merge Worst: %.2gs" % (end-start)

    a = [i for i in xrange(size)]
    print "Best Case"

    start = time.clock()
    merge_sort(a, 0, size-1)
    end = time.clock()
    print "Merge Best: %.2gs" % (end-start)


if __name__ == '__main__':
    size = 2000
    print "Size: "+str(size)
    time_track(size)

    sort_me = [5,4,1,13,8,7,2,6,3]
    merge_sort(sort_me, 0, 8)
    for item in sort_me:
        print item,
    print
    unsort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    unsort_repeated = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9]
    sorted_repeated = [9, 9, 9, 9, 9, 10, 10, 10, 10, 10]
    merge_sort(unsort, 0, 9)
    merge_sort(unsort_repeated, 0, 9)
    print unsort == sort
    print unsort_repeated == sorted_repeated





