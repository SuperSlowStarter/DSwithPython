import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import networkx as nx

# 한글 폰트 설정
font_path = 'C:\Windows\Fonts\H2GTRM.TTF'  # 설치된 NanumGothic 폰트의 경로
fontprop = fm.FontProperties(fname=font_path)

plt.rc('font', family='HYGothic 중간')
plt.rcParams['axes.unicode_minus'] = False

## 함수 선언 부분 ##
class TreeNode() :
    def __init__(self) :
        self.left = None
        self.data = None
        self.right = None

## 전역 변수 선언 부분 ##

root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인 코드 부분 ##
node = TreeNode()
node.data = nameAry[0]
root = node

for name in nameAry[1:] :
    node = TreeNode()
    node.data = name

    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

# Visualization helper functions
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        pos[node.data] = (x, y)
        if node.left is not None:
            graph.add_edge(node.data, node.left.data)
            add_edges(graph, node.left, pos, x - 1 / layer, y - 1, layer + 1)
        if node.right is not None:
            graph.add_edge(node.data, node.right.data)
            add_edges(graph, node.right, pos, x + 1 / layer, y - 1, layer + 1)

def draw_bst(root):
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, root, pos)
    plt.figure(figsize=(10, 6))
    nx.draw(graph, pos, with_labels=True, arrows=False, node_size=2000, font_size=10)
    plt.title("Binary Search Tree Structure")
    plt.show()

# Draw the BST


def deleteBST(deleteName):
    current = root
    parent = None
    while True :
        if deleteName == current.data :
            if current.left == None and current.right == None :
                if parent.left == current :
                    parent.left = None
                else :
                    parent.right = None
                del(current)
            
            elif current.left != None and current.right == None :
                if parent.left == current :
                    parent.left = current.left
                else :
                    parent.right = current.left
                del(current)
            
            elif current.left == None and current.right != None :
                if parent.left == current :
                    parent.left = current.right
                else :
                    parent.right = current.right
                del(current)
            
            print(deleteName, '이(가) 삭제됨.')
            break
        
        elif deleteName < current.data :
            if current.left == None :
                print(deleteName, '이(가) 트리에 없음')
                break
            parent = current
            current = current.left
        else :
            if current.right == None :
                print(deleteName, '이(가) 트리에 없음')
                break
            parent = current
            current = current.right

deleteBST("마마무")

draw_bst(root)