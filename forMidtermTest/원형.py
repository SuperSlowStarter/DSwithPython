class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes():
    current = head
    if current.data == None:
        return
    print(current.data, end=" ")
    while current.link != head:
        current = current.link
        print(current.data, end=" ")



dataArray = ["다혀","정여","즈위","산자","지호"]
head, prev, current = None, None, None

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head

    for data in dataArray[1:]:
        prev = node
        node = Node()
        node.data = data
        prev.link = node
        node.link = head

    printNodes()