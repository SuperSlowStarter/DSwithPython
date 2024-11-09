class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def findVertex(g, findVtx):
    stack = []
    visitedAry = []

    current = 0
    stack.append(current)
    visitedAry.append(current)

    while (len(stack) != 0):
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] == 1:
                if vertex in visitedAry:
                    pass
                else:
                    next = vertex
                    break

        if next != None:
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False

gSize = 6
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0, 1, 2, 3, 4, 5
names = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']

G1 = Graph(gSize)
G1.graph[문별][솔라] = 1; G1.graph[문별][휘인] = 1
G1.graph[솔라][문별] = 1; G1.graph[솔라][쯔위] = 1
G1.graph[휘인][문별] = 1; G1.graph[휘인][쯔위] = 1
G1.graph[쯔위][솔라] = 1; G1.graph[쯔위][휘인] = 1; G1.graph[쯔위][선미] = 1
G1.graph[선미][쯔위] = 1

friend = 화사
contactable = findVertex(G1, friend)
if contactable:
    print(f'{names[friend]} 연락이 됨')
else:
    print(f'{names[friend]} 연락이 안됨')

friend = 선미
contactable = findVertex(G1, friend)
if contactable:
    print(f'{names[friend]} 연락이 됨')
else:
    print(f'{names[friend]} 연락이 안됨')
