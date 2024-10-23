class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start): #current부터 출력하는 함수#
    current = start #current지시봉
    if current is None: #아무것도 없으면 아웃
        return
    print(current.data, end=' -> ')
    while current.link is not None: #current에 뭐가 잡히면
        current = current.link
        print(current.data, end=' -> ')
    print()

def makeSimpleLinkedList(namePhone): #linkedlist만드는 함수#
    global head, current, prev
    printNodes(head) ##이거 뭐하는과정?
    node = Node()
    node.data = namePhone
    if head is None:
        head = node
        return
    if head.data[0] > node.data[0]:
        node.link = head
        head = node
        return
    current = head
    while current.link is not None:
        prev = current
        current = current.link
        if current.data[0] > node.data[0]:
            prev.link = node
            node.link = current
            return
    current.link = node





head, current, prev = None, None, None
dataArray = [['지민, 1'], ['정국, 2'],['뷔, 3'],['슈가, 4'],['진, 5']]

if __name__ == "__main__":
    for data in dataArray:
        makeSimpleLinkedList(data)
    printNodes(head)

