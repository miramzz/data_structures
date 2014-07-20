

def merge(sort_me, f_index, m_index, l_index):
    tmp_index = m_index-1
    while m_index >= f_index:
        if sort_me[m_index]>sort_me[m_index+1]:
            sort_me[m_index], sort_me[m_index+1] = sort_me[m_index+1], sort_me[m_index]
            m_index += 1
            if m_index == l_index:
                m_index = tmp_index
                tmp_index -= 1
        else:
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
    # size = 20000
    # print "Size: "+str(size)
    # time_track(size)

    sort_me = [5,4,1,13,8,7,2,6,3]
    merge_sort(sort_me, 0, 8)
    for item in sort_me:
        print item,





