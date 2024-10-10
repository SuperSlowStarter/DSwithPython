#기본 노드 형태 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#노드들을 append()로 추가하면서 head와tail을 세팅. 동시에 prev와 next를 세팅
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data): 
        new_node = Node(data) #노드 만들때 데이터도 넣어진다

        if self.head is None: #아무것도 없으면 새 노드가 처음이자 끝
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node #끝의 다음은 새것
            new_node.prev = self.tail #지금 끝에있는게 새것의 전
            self.tail = new_node #모든것의 끝은 새것


##프린트함수##
def printNodes(dll: DoubleLinkedList): #이중연결리스트 클래스를 받는다
    current = dll.head #head를 가리키는 current지시봉 
    print("정방향-->",  end=' ')
    while current: #다음노드가 존재한다면
        print(current.data, end=' ')
        current = current.next
    print()
    print("역방향-->",  end=' ')
    current = dll.tail
    while current:
        print(current.data, end=' ')
        current = current.prev

#메인코드시작
if __name__ == "__main__":
    twice = ["다현", "정연", "쯔위", "사나", "지효"]
    my_linked_list = DoubleLinkedList()

    for member in twice:
        my_linked_list.append(member)

    printNodes(my_linked_list)
