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

######################이진탐색트리 구성#####################
node = TreeNode()
node.data = nameAry[0]
root = node

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    current = root

    while True:
        if name < current.data:
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
############################################################



print(nameAry)
findName = "마마"

current = root
while True:
    if findName == current.data:
        print(findName, " 찾음.")
        break
    elif findName < current.data:
        if current.left == None:
            print("이거 없어요.")
            break
        current = current.left
    else:
        if current.right == None:
            print("이거 없어요.")
            break
        current = current.right

deleteName = input("삭제하려는 이름 입력 >> ")

current = root
parent = None
while True:
    if deleteName == current.data:
        if current.left == None and current.right == None:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del(current)
        elif current.left != None and current.right == None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del(current)
        elif current.left == None and current.right != None:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
            del(current)
        print(deleteName, " 삭제함.")
        break
    elif deleteName < current.data:
        if current.left == None:
            print(deleteName, '가 트리에 없음.')
            break
        parent = current
        current = current.left
    else:
        if current.right == None:
            print(deleteName, '가 트리에 없음.')
            break
        parent = current
        current = current.right