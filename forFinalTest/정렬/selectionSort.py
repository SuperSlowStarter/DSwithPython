def findMinIndex(ary):
    minIndex = 0
    for i in range(1, len(ary)):
        if(ary[minIndex] > ary[i]):
            minIndex = i
    return minIndex

before = [188,162,168,120,50,150,177,105]
after = []

print(before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print(after)