class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "민지"
node1.link = node2

node3 = Node()
node3.data = "고려"
node2.link = node3

node4 = Node()
node4.data = "미나"
node3.link = node4

node5 = Node()
node5.data = "기완"
node4.link = node5

print(node1.data, end = " ")
print(node1.link.data, end = " ")
print(node1.link.link.data, end = " ")
print(node1.link.link.link.data, end = " ")
print(node1.link.link.link.link.data, end = " ")
