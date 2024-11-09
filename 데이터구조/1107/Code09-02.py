## 클래스와 함수 선언 부분 ##
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# def printGraph(g):
#     print(' ', end = ' ')
#     for v in range(g.SIZE):
#         print(nameAry[v], end = ' ')
#     print()
#     for row in range(g.SIZE):
#         print(nameAry[row], end = ' ')
#         for col in range(g.SIZE):
#             print(g.graph[row][col], end = ' ')
#         print()
#     print()

def printGraph(g):
    # 첫 번째 행: 이름 출력
    print('      ', end='')  # 첫 번째 열의 공백 맞추기
    for v in range(g.SIZE):
        print(f"{nameAry[v]:<6}", end='')  # 노드 이름을 6칸 고정으로 출력
    print()
    
    # 각 행의 내용 출력
    for row in range(g.SIZE):
        print(f"{nameAry[row]:<6}", end='')  # 왼쪽 이름을 6칸 고정으로 출력
        for col in range(g.SIZE):
            print(f"{g.graph[row][col]:<8}", end='')  # 값은 8칸 고정으로 출력
        print()
    print()

## 전역 변수 선언 부분 ##
G1 = None
nameAry = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0,1,2,3,4,5

## 메인 코드 부분 ##
gSize = 6
G1 = Graph(gSize)
G1.graph[문별][솔라] = 1; G1.graph[문별][휘인] = 1
G1.graph[솔라][문별] = 1; G1.graph[솔라][쯔위] = 1
G1.graph[휘인][문별] = 1; G1.graph[휘인][쯔위] = 1
G1.graph[쯔위][솔라] = 1; G1.graph[쯔위][휘인] = 1; G1.graph[쯔위][선미] = 1; G1.graph[쯔위][화사] = 1
G1.graph[선미][쯔위] = 1; G1.graph[선미][화사] = 1
G1.graph[화사][쯔위] = 1; G1.graph[화사][선미] = 1

print("## G1 무방향 그래프 ##")
printGraph(G1)

