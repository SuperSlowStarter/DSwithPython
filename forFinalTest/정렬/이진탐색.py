def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary) - 1

    while (start <= end):
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid+1
        else:
            end = mid -1

    return pos