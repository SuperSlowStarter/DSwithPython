## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData :
        current = head = head.link
        del(current)
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def insertNode(findData, insertData) :
    global memory, head, current, pre

    if head.data == findData :
        node=Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None :
        pre = current
        current = current.link

        if current.data == findData:
            node=Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    node = Node()
    node.data = insertData
    current.link = node

## 전역 변수 선언 부분 ##

head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__":
    node = Node()  # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    

    for data in dataArray[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        

    printNodes(head)

    
    deleteNode("다현")
    printNodes(head)
    deleteNode("쯔위")
    printNodes(head)
    deleteNode("지효")
    printNodes(head)
    deleteNode("재남")
    printNodes(head)
    

