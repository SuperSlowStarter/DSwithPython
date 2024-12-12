class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

#inorder
#predorder
#postorder

root = None
nameAry = ['블핑', '레벨', '마마', '에이', '걸스', '트와']

node = TreeNode()
node.data = nameAry[0]
root = node

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    current = root

    while True:
        if name < current:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

print("이진 탐색 트리 구성 완료!")