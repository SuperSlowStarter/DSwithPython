from tkinter import *

window = Tk()
window.geometry("600x600")

photo = PhotoImage(file='C:/Users/daegu/OneDrive/바탕 화면/파이썬/데이터구조/1128/cat.gif')


photoAry =[]
height = photo.height()
width = photo.width()
for i in range(height):
    for k in range(width):
        r, g, b = photo.get(k, i) #파이썬의 get(x, y)로 써야 한다. 따라서 너비 * 높이 로 해야 한다.
        value = (r + g + b) // 3
        photoAry.append(value)


def qSort(arr, start, end):
    if end <= start:
        return

    low = start
    high = end

    pivot = arr[(low + high) // 2]  # 작은 값은 왼쪽, 큰 값은 오른쪽으로 분리
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    mid = low

    qSort(arr, start, mid - 1)
    qSort(arr, mid, end)

def quickSort(ary):
    qSort(ary, 0, len(ary)-1)

def blackScaling () :
    for i in range(len(photoAry)):
        if photoAry[i] <= midValue:
            photoAry[i] = 0
        else:
            photoAry[i] = 255

    position = 0
    for i in range(height):
        for k in range(width):
            r = g = b = photoAry[position]
            position += 1
            photo.put("#%02x%02x%02x" % (r, g, b), (k, i))


dataAry = photoAry[:]
quickSort(dataAry)
midValue = dataAry[height*width // 2]
print(midValue)



blackScaling()
paper = Label(window, image=photo)
paper.pack(expand=1, anchor=CENTER)
window.mainloop()

#1차원 배열에는 rgb값의 평균으로 저장함
