class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = None
nameAry = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0,1,2,3,4,5

gSize = 6
G1 = Graph(gSize)
G1.graph[문별][솔라] = 10; G1.graph[문별][휘인] = 15
G1.graph[솔라][문별] = 10; G1.graph[솔라][휘인] = 40; G1.graph[솔라][쯔위] = 11; G1.graph[솔라][4] = 50
G1.graph[휘인][문별] = 15; G1.graph[휘인][솔라] = 40; G1.graph[휘인][쯔위] = 12
G1.graph[쯔위][솔라] = 11; G1.graph[쯔위][휘인] = 12; G1.graph[쯔위][4] = 20; G1.graph[쯔위][5] = 30
G1.graph[선미][솔라] = 50; G1.graph[선미][쯔위] = 20; G1.graph[선미][5] = 25
G1.graph[화사][쯔위] = 30; G1.graph[화사][선미] = 25

#가중치 간선 별도 배열
edgeAry = []
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:
            edgeAry.append([G1.graph[i][k], i, k]) #[가중치, 출발, 도착]

from operator import itemgetter
edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=True) #가중치 기준으로 정렬하겠다

#중복제거
sortedAry = []
for i in range(0, len(edgeAry), 2):
    sortedAry.append(edgeAry[i])

#가중치 높은 간선 제거
index = 0

start = sortedAry[index][1]
end = sortedAry[index][2]