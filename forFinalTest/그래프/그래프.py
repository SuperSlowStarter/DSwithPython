#정점 생성
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]

G1, G3 = None, None

#정점 연결
G1 = Graph(4)
G1.graph[0][1] = 1 #이 1이 나중에는 가중치가 되는거지
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][0] = 1
G1.graph[1][0] = 1


for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end=' ')
    print()