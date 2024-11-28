class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(0)
        else:
            raise IndexError("pop from empty stack")
        
    def peek(self):
        if not self.is_empty():
            return self.stack[0]
        else:
            raise IndexError("peek from empty stack")
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.peek())
    print(s.pop())
    print(s.size())
    print(s.is_empty())