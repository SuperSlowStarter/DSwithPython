def BubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYN = False
        print('사이클--> ', ary)

        for cur in range(0, end):
            if (ary[cur]>ary[cur+1]):
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True
        if not changeYN: #초기화를 False로 했기 때문에 if not changeYN 이 True면
            break

    return ary

dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

print('정렬 전 --> ', dataAry)
afterBubbleSortAry = BubbleSort(dataAry)
print('정렬 gn --> ', afterBubbleSortAry)