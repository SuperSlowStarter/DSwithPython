class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

root = None #root는 머지?
nameArray = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

#첫 번째 데이터 삽입
node = TreeNode()
node.data = nameArray[0]
root = node

name = '레드벨벳'
node =  TreeNode()
node.data = name
current = root
if name < current.data:
    current.left = node
else:
    current.right = node

#반복적으로 자기 자리 찾아가기??
name = 6
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