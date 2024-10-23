class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(head):
    current = head
    if current == None:
        return
    print(current.data, end=" ")
    while current.link != None: #끝날때까지
        current = current.link
        print(current.data, end=" ")
    print()

if __name__ == "__main__":

    head, current, pre = None,None,None
    dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

    node = Node()
    node.data = dataArray[0] #첫 노드 만들기
    head = node #헤드포인터 노드가르키기

    for data in dataArray:
        pre = node #전노드는 첫노드
        newNode = Node() #새노드 생성
        newNode.data = data #새노드 데이터는 새데이터
        pre.link = newNode #전꺼 링크는 이번노드


#여기까지 노드가 생성되었고, 이제 프린트
    printNodes(head)