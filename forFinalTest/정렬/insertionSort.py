def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if (ary[cur-1] > ary[cur]):
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
    return ary