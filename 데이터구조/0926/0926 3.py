class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def print_all_nodes () :
    current = node1
    print(current.data, end=' => ')
    while current.link is not None:
        current = current.link
        if current.link is None:
            print(current.data)
        else:
            print(current.data, end=" => ")

def insert_new_node(previous_node, node):
    node.link = previous_node.link
    previous_node.link = node

node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node() #노드 생성
node4.data = "사나" #노드 데이터 할당
node3.link = node4 #링크

node5 = Node()
node5.data = "지효"
node4.link = node5

print_all_nodes()

node2a = Node()
node2a.data = "재남"
insert_new_node(node2, node2a)
print_all_nodes()