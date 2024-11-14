def openBox() :
    global count
    print("종이 상자를 엽니다. ^^")
    count -= 1
    if count == 0:
        print("반지를 반환합니다.")
        return #리턴이 이루어지면 0이 되지 않을 떄는 
    openBox()
    print(("종이 상자를 닫습니다."))


count = 10
openBox()