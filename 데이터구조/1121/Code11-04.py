def findInsertIdx(ary, data) :
    findIdx = -1                     # 초기값은 없는 위치로 설정
    for i in range(0, len(ary)) :
        if (ary[i] > data) :
            findIdx = i
            break

    if findIdx == -1 :                # 큰 값을 못 찾으면 끝까지 가야 함
        return len(ary)
    else :
        return findIdx

testAry = []
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 -->', insPos)

testAry = [33, 77, 88]
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 -->', insPos)

testAry = [33, 55, 77, 88]
insPos = findInsertIdx(testAry, 100)
print('삽입할 위치 -->', insPos)
