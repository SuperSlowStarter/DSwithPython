def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE-1):
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print("큐가 꽉 찾습니다.")
        return
    
def deQueue(data):
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다!")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty):
        print("큐가 비었습니다.")
        return None
    return queue[frint+1]

SIZE = int(input("큐 크기를 입력하세요==>"))
queue = [None for _ in range(SIZE)]
front = rear = 1

if __name__ == "__main__":
    select = input("삽입, 추추르 확이느 종료 중 하나를 선택==>")

    while(select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            enQueue(data)
            print("큐 상태 : ", queue)
        elif select == 'E' or select == 'e':
            data = deQueue()