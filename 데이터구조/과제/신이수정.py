# 전역 변수 선언 #
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]
head, current, prev = None, None, None

class Node():
    def __init__ (self) :        
        self.data = None
        self.link = None
        self.plink = None
 
def printForwardNodes(start) :
    global current
    current = start
    print("정방향 -->", current.data, end = ' ')
    while current.link != None : #이제 원형리스트가 아니니까 head가 아니야
        current = current.link
        print(current.data, end = ' ')

def printBackwardNodes(current) : #current가 직접 파라미터가 되 (43줄 참조)
    #current = last
    print("역방향 -->", current.data, end = ' ')
    while current.plink != None :
        current = current.plink
        print(current.data, end = ' ')

# 메인 함수 #
if __name__ == "__main__" :
    node = Node()
    node.data = dataArray[0] #첫 노드 생성
    head = node

    for data in dataArray[1:] :
        prev = node
        node = Node()
        node.data = data  #node 생성
        prev.link = node  #전 노드를 새 노드에 링크
        node.plink = prev #노드의 이전 노드 링크 설정
        #node.link = head  #새 노드가 헤드를 가리킴

    printForwardNodes(head)
    print('') #줄 바꿈
    #head = current #역방향 출력 전 head를 가장 끝 노드로 설정
    printBackwardNodes(current) ###current를 global로 선언햇기 때문에 이미 last로 가있어
