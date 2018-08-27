# -*- coding: utf-8 -*-
def Insertion_sort(l):
    '''Sort a list using insert method.

    :type l: list[int]
    :rtype None return
    '''
    for j in range(1,len(l)):
        key = l[j]
        i = j - 1
        while i >= 0 and l[i] > key:
            l[i+1] = l[i]
            i -= 1
        l[i+1] = key

def Merge_sort(l,*args):
    """sort a list using merge method

    :param l: list[int] the sorting list
    :return: None
    """
    def Merge(l, p, q, r):
        """Merge two sorted list into one

        :param l: list[int] the sorting list
        :param p: int begin index
        :param q: int middle index
        :param r: int end index
        :return: None
        """
        la = l[p:q+1]
        ra = l[q+1:r+1]
        la.append(float('inf'))
        ra.append(float('inf'))
        i = j = 0
        for index in range(p, r+1):
            if la[i] <= ra[j]:
                l[index] = la[i]
                i += 1
            else:
                l[index] = ra[j]
                j += 1
    if args:
        p, r = args
    else:
        p, r = 0, len(l)-1
    if p < r:
        q = (p+r)/2
        Merge_sort(l, p, q)
        Merge_sort(l, q+1, r)
        Merge(l, p, q, r)
