#!/usr/bin/python


def insertion_sort(sort_me):
    for i in range(len(sort_me)):
        j = i
        while j-1 >= 0 and sort_me[j] < sort_me[j-1]:
            sort_me[j-1], sort_me[j] = sort_me[j], sort_me[j-1]
            j -= 1
    #return sort_me

