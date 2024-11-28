## 클래스와 함수 선언 부분 ##
class Graph():  # 그래프 클래스 정의
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]  # size x size 배열 생성, 0으로 초기화

def printGraph(inputGraph):
    print("         ", end='')
    for v in range(inputGraph.SIZE):  # 도시 이름을 출력하기 위해 반복
        print(f"{locationDict[v]:^4}", end=' ')  # 도시 이름을 폭 4에 가운데 정렬
    print()
    for row in range(inputGraph.SIZE):  # 각 도시의 가중치를 출력
        print(f"{locationDict[row]:<6}", end=' ')  # 도시 이름을 폭 6에 왼쪽 정렬
        for col in range(inputGraph.SIZE):  # 각 도로의 가중치 출력
            print(f"{inputGraph.graph[row][col]:^6}", end=' ')  # 가중치를 폭 6에 가운데 정렬
        print()  # 한 행 출력이 끝났으므로 줄바꿈
    print()

def findVertex(g, findVtx):
    stack = []  # 탐색에 사용할 스택 초기화
    visitedAry = []  # 방문한 정점 저장용 배열 초기화

    current = 0  # 시작 정점을 0으로 설정 (서울)
    stack.append(current)  # 시작 정점을 스택에 추가
    visitedAry.append(current)  # 시작 정점을 방문 배열에 추가

    while len(stack) != 0:  # 스택이 비어있지 않은 동안 반복
        next_vertex = None  # 다음 방문할 정점 초기화
        for vertex in range(gSize):  # 현재 정점에서 모든 정점 탐색
            if g.graph[current][vertex] != 0:  # 간선이 존재하는 경우
                if vertex in visitedAry:  # 이미 방문했으면 건너뜀
                    pass
                else:
                    next_vertex = vertex  # 방문하지 않은 정점을 다음 정점으로 지정
                    break  # 첫 번째 방문하지 않은 정점 찾으면 종료

        if next_vertex is not None:  # 다음 방문할 정점이 있으면
            current = next_vertex  # 현재 정점을 업데이트
            stack.append(current)  # 스택에 현재 정점 추가
            visitedAry.append(current)  # 방문 배열에 추가
        else:
            current = stack.pop()  # 다음 정점 없으면 스택에서 pop하여 되돌아감

    return findVtx in visitedAry  # 목표 정점이 방문 배열에 있으면 True 반환

## 전역 변수 선언 부분 ##
G1 = None
locationDict = {0: '서울', 1: '뉴욕', 2: '런던', 3: '북경', 4: '방콕', 5: '파리'}  # 숫자와 지역 매칭

## 메인 코드 부분 ##
gSize = 6
G1 = Graph(gSize)
G1.graph[0][1] = 80; G1.graph[0][4] = 10
G1.graph[1][0] = 80; G1.graph[1][3] = 40; G1.graph[1][4] = 70
G1.graph[2][4] = 30; G1.graph[2][5] = 60
G1.graph[3][0] = 10; G1.graph[3][1] = 40; G1.graph[3][4] = 50
G1.graph[4][1] = 70; G1.graph[4][3] = 50; G1.graph[4][2] = 30; G1.graph[4][5] = 20
G1.graph[5][4] = 20; G1.graph[5][2] = 60

print("## 해저 케이블 연결을 위한 전체 연결도 ##")
printGraph(G1)

# 가중치 간선 목록
edgeAry = []  # 간선 리스트 초기화
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:  # 가중치가 0이 아닌 경우에만 간선 추가
            edgeAry.append([G1.graph[i][k], i, k])  # [가중치, 출발 정점, 도착 정점]으로 간선 리스트에 추가

from operator import itemgetter

edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=False)  # 가중치 기준 오름차순 정렬

# 중복 간선 제거 작업
realEdgeAry = []
for i in range(0, len(edgeAry), 2):  # 왕복 간선 중 하나씩만 남기기 위해 두 칸씩 건너뜀
    realEdgeAry.append(edgeAry[i])

index = 0
while len(realEdgeAry) > gSize - 1:  # 간선 개수가 '정점 개수-1'일 때까지 반복
    start = realEdgeAry[index][1]  # 시작 정점
    end = realEdgeAry[index][2]  # 도착 정점
    saveCost = realEdgeAry[index][0]  # 가중치 저장

    G1.graph[start][end] = 0  # 간선을 임시로 제거
    G1.graph[end][start] = 0

    startYN = findVertex(G1, start)  # 시작 정점이 연결되어 있는지 확인
    endYN = findVertex(G1, end)  # 도착 정점이 연결되어 있는지 확인

    if startYN and endYN:  # 두 정점이 모두 연결되어 있다면
        del realEdgeAry[index]  # 해당 간선을 리스트에서 제거하여 사이클 방지
    else:
        G1.graph[start][end] = saveCost  # 간선 복구
        G1.graph[end][start] = saveCost  # 양방향 연결 복구
        index += 1  # 다음 간선을 확인하기 위해 인덱스 증가

print("## 가장 효율적인 해저 케이블 연결도 ##")
printGraph(G1)  # 최종적으로 최소 비용의 연결도 출력
