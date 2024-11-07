class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(head):
    current = head
    if current.link == None:
        return
    print(current.data, end=" ")
    while current.link != head:
        current = current.link
        print(current.link, end=" ")
    print()

def insertNode(findData, insertData):
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return
    
    current=head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node=Node()
            node.data = insertData
            node.link=current
            pre.link=node
            return
        
    node = Node()
    node.data = insertData
    current.link = node
    node.link = head

def deleteNode(deleteData):
    if head.data == deleteData:
        current = head
        head = head.link #마지막을 찾으러 갈거에요
        while last.link != current: #마지막의 다음이 지금일때까지
            last = last.link #last를 넘겨
            #찾으면
        last.link = head
        del(current)
        return
    
    current.head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return


head, current, pre = None, None, None
dataArray = ["다현","정연","쯔위","사나","지효"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head

    printNodes()