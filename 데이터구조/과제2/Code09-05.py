###############최소 비용 신장 트리(MST)###############


class Graph() : #그래프 클래스 정의
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)] #초기화 시 size 차원 배열 생성, 0 으로 채워진다

def printGraph(inputGraph):
    print(' ', end=' ')
    for v in range(inputGraph.SIZE): #6*6 배열이니까 6번
        print(nameAry[v], end=' ')
    print()
    for row in range(inputGraph.SIZE): #지역명
        print(nameAry[row], end=' ')
        for col in range(inputGraph.SIZE): #각 도로 가중치 출력
            print(inputGraph.graph[row][col], end=' ')
        print() # 한 지역 출력이 끝났으니 엔터
    print() 

def findVertex(g, findVtx):
    stack = [] # 탐색에 사용할 스택을 초기화
    visitedAry = [] # 방문한 정점들을 저장할 배열을 초기화

    current = 0  # 시작 정점을 0으로 설정 (춘천)
    stack.append(current)  # 시작 정점을 스택에 추가
    visitedAry.append(current)  # 시작 정점을 방문 배열에 추가

    # 스택이 비어있지 않은 동안 반복 (탐색이 끝날 때까지)
    while (len(stack) != 0):
        next = None                           # 다음에 방문할 정점을 초기화
        for vertex in range(gSize):           # 현재 정점에서 모든 정점에 대해 반복
            if g.graph[current][vertex] != 0: # 현재-vertex 간에 간선이 존재하는지 확인
                if vertex in visitedAry:      # 이미 방문한 정점인지 확인
                    pass                      # 방문했다면 넘어감
                else:
                    next = vertex             # 방문하지 않은 정점을 다음 방문 정점으로 지정
                    break                     # 첫 방문하지 않은 정점을 찾으면 반복 종료

        if next != None:                      # 방문할 다음 정점이 있다면
            current = next                    # 현재 정점을 다음 정점으로 이동
            stack.append(current)             # 스택에 현재 정점을 추가
            visitedAry.append(current)        # 방문 배열에 현재 정점을 추가
        else:
            current = stack.pop()             # 다음 방문할 정점이 없으면 스택에서 pop하여 되돌아감

    if findVtx in visitedAry:                 # 목표 정점이 방문 배열에 있으면
        return True                           # 해당 정점이 연결되어 있음을 의미하여 True 반환
    else:
        return False                          # 연결되지 않았다면 False 반환

    
## 전역 변수 선언 부분 ##
G1 = None
nameAry = {0: '춘천', 1: '서울', 2: '속초', 3: '대전', 4: '광주', 5: '부산'} #딕셔너리를 이용해 숫자와 지역 매칭

###################
## 메인 코드 부분 ##
###################

gSize = 6
G1 = Graph(gSize)
G1.graph[0][1] = 10; G1.graph[0][2] = 15
G1.graph[1][0] = 10; G1.graph[1][2] = 40; G1.graph[1][3] = 11; G1.graph[1][4] = 50
G1.graph[2][0] = 15; G1.graph[2][1] = 40; G1.graph[2][3] = 12
G1.graph[3][1] = 11; G1.graph[3][2] = 12; G1.graph[3][4] = 20; G1.graph[3][5] = 30
G1.graph[4][1] = 50; G1.graph[4][3] = 20; G1.graph[4][5] = 25
G1.graph[5][3] = 30; G1.graph[5][4] = 25

print('## 자전거 도로 건설을 위한 전체 연결도 ##')
printGraph(G1)

# 가중치 간선 목록
edgeAry = [] #빈 간선배열
for i in range(gSize) :
    for k in range(gSize) : #가중치가 0이 아니면 간선배열에 추가
        if G1.graph[i][k] != 0 :
            edgeAry.append([G1.graph[i][k], i, k]) #간선배열에 저장되는 값 [가중치, 출발지역, 도착지역]
            ## 추가가 완료된 후 edgeAry 상태
            ##edgeAry = [[10, 0, 1], [15, 0, 2], [10, 1, 0], [40, 1, 2], [11, 1, 3], [50, 1, 4], [15, 2, 0], [40, 2, 1], [12, 2, 3], [11, 3, 1], [12, 3, 2], [20, 3, 4], [30, 3, 5], [50, 4, 1], [20, 4, 3], [25, 4, 5], [30, 5, 3], [25, 5, 4]]

from operator import itemgetter


edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=True) # "간선배열을, key=itemgetter(가중치)기준으로, 내림차순으로 sort한다"
## itemgetter : 특정 인덱스나 키에 따라 요소를 가져오는 기능
## 각 요소가 [가중치, 시작지역, 도착지역] 이므로, itemgetter(0)은 각 요소의 첫 번째 값인 가중치를 가져온다
## 따라서 정렬이 완료되면 가중치가 큰 순서대로 내림차순(reverse = True)으로 정렬된다


######## 중복 제거작업 ########
realEdgeAry = []
for i in range(0, len(edgeAry), 2) : #리스트를 두 칸씩 건너뛰면서 반복 why? 왕복으로 판정되어서 간선이 두개씩 생겼기 때문
    realEdgeAry.append(edgeAry[i])
##############################

index = 0
while (len(realEdgeAry) > gSize-1) :    # 간선 개수가 '정점 개수-1'일 때까지 반복
    start = realEdgeAry[index][1]       ##가중치간선배열 index번째 항목의 시작지역
    end = realEdgeAry[index][2]         ##가중치간선배열 index번째 항목의 도착지역
    saveCost = realEdgeAry[index][0] ##가중치간선배열 index번째 항목의 가중치
## 완료 후
## realEdgeary = [[50, 1, 4], [40, 1, 2], [30, 3, 5], [25, 4, 5], [20, 3, 4], [15, 0, 2], [12, 2, 3], [11, 1, 3], [10, 0, 1]]
    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

startYN = findVertex(G1, start)         # 시작 정점이 연결되어 있는지 확인 (서브그래프에 포함 여부)
endYN = findVertex(G1, end)             # 도착 정점이 연결되어 있는지 확인 (서브그래프에 포함 여부)

if startYN and endYN:                   # 시작 정점과 도착 정점 모두 연결되어 있다면
    del(realEdgeAry[index])             # 해당 간선을 삭제하여 연결하지 않음 (사이클 방지)
else:
    G1.graph[start][end] = saveCost     # 간선을 복구하여 자전거 도로로 연결
    G1.graph[end][start] = saveCost     # 양방향 연결이므로 반대쪽 간선도 복구
    index += 1                          # 다음 간선을 확인하기 위해 인덱스를 증가시킴

print('## 최소 비용의 자전거 도로 연결도 ##')
printGraph(G1)                          # 최종적으로 최소 비용 연결도를 출력

