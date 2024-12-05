import random

## Function Definitions ##
def seqSearch(ary, fData):
    global count
    pos = -1
    for i in range(len(ary)):
        count += 1
        if ary[i] == fData:
            pos = i
            break
    return pos

def binSearch(ary, fData):
    global count
    start = 0
    end = len(ary) - 1

    while start <= end:
        count += 1
        mid = (start + end) // 2

        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

## Global Variables ##
dataAry, sortedAry = [], []
findData = 7878
count = 0

## Main Code ##
dataAry = [random.randint(0, 999999) for _ in range(1000000)]
dataAry.insert(random.randint(0, 1000000), findData)
sortedAry = sorted(dataAry)

print("#Unsorted Array (1,000,000) -->", dataAry[:5], '...', dataAry[-5:])
print("#Sorted Array (1,000,000) -->", sortedAry[:5], '...', sortedAry[-5:])

count = 0
pos = seqSearch(dataAry, findData)
if pos != -1:
    print('Sequential Search (Unsorted Data) -->', count, 'iterations')

count = 0
pos = binSearch(sortedAry, findData)
if pos != -1:
    print('Binary Search (Sorted Data) -->', count, 'iterations')
