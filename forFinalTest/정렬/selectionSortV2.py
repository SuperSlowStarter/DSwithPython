def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIndex = i
        for k in range(i+1, n):
            if (ary[minIndex] > ary[k]):
                minIndex = k
        tmp = ary[i]
        ary[i] = ary[minIndex]
        ary[minIndex] = tmp

    return ary

dataAry = [321,4321,34,234,23,2543,4343,5,6,7]

print(dataAry)
dataAry = selectionSort(dataAry)
print(dataAry)