# -*- coding: utf-8 -*-
from Sorts import *
import time
import random

def ge_list(n):
    l = []
    for i in range(n):
        l.append(random.randint(1, 10000))
    return l

if __name__ == '__main__':
    # print 'Please insert a list of ints'
    # int_s = raw_input()
    # int_l = [int(i) for i in int_s.split()]
    int_l = ge_list(200000)
    # print 'before ', int_l
    now = time.time()
    Merge_sort(int_l)
    # print 'Merge: ', int_l
    af_mer = time.time()
    print "Merge-sort cost ", af_mer-now, ' seconds.'
    Insertion_sort(int_l)
    # print 'Insertion: ', int_l
    af_ins = time.time()
    print "Insertion-sort cost ", af_ins - af_mer, ' seconds.'
