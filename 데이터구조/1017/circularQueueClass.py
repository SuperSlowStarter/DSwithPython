class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        if self.front == self.rear:  # 큐가 비게 되는 경우
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0
        return (self.rear - self.front + self.capacity) % self.capacity + 1

    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        i=self.front
        while True:
            items.append(self.queue[i])
            if i==self.rear:
                break
            i=(i+i)%self.capacity
        return str(items)

if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)

    print("원형 큐의 상태:", cq)
    print("큐의 크기: ", cq.size())

    print("Dequeue: ", cq.dequeue())
    print("원형 큐 상태: ", cq)

    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)

    print("원형 큐 상태: ", cq)
    print("Peek: ", cq.peek())

    cq.dequeue()
    cq.dequeue()

    print("원형 큐 상태: ", cq)

    cq.enqueue(7)
    print("원형 큐 상태: ", cq)
