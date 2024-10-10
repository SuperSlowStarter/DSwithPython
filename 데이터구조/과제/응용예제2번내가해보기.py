# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data  # 데이터 저장
        self.prev = None  # 이전 노드에 대한 포인터
        self.next = None  # 다음 노드에 대한 포인터

# 이중 연결 리스트 클래스 정의
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 헤드 노드

    # 노드 추가 메서드
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # 헤드가 없는 경우, 새 노드를 헤드로 지정
            self.head = new_node
            return
        # 마지막 노드 찾기
        last = self.head
        while last.next:
            last = last.next
        # 마지막 노드에 새 노드 연결
        last.next = new_node
        new_node.prev = last

    # 정방향 출력 메서드
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # 역방향 출력 메서드
    def print_backward(self):
        current = self.head
        # 마지막 노드까지 이동
        while current and current.next:
            current = current.next
        # 역방향으로 이동하며 출력
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# 이중 연결 리스트 생성
dll = DoublyLinkedList()

# 이미지의 순서대로 노드 추가
nodes = ["다현", "정연", "쯔위", "사나", "지효"]
for node in nodes:
    dll.append(node)

# 정방향 출력
print("정방향 출력: ", end="")
dll.print_forward()

# 역방향 출력
print("역방향 출력: ", end="")
dll.print_backward()
