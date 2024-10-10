import webbrowser
import time

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


# 메인 코드 부분
if __name__ == "__main__":
    urls = ['naver.com', 'daum.net', 'nate.com']
    s = Stack()

    for url in urls:
        s.push(url)
        webbrowser.open('http://' + url)
        print(url, end='-->')
        time.sleep(1)

    print("방문 종료")
    time.sleep(5)

    while True:
        url = s.pop()
        if s.is_empty():
            break
        webbrowser.open('http://' + url)
        print(url, end='-->')
        time.sleep(1)
    print("방문 종료")
