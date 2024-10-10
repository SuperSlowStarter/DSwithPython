class Stack:
    def __init__(self):  # 빈 스택 초기화
        self.stack = []

    def push(self, item):  # 아이템을 스택에 추가
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self):  # 스택이 비어있는지 확인
        return len(self.stack) == 0


def is_balanced(expression):
    stack = Stack()
    bracket_map = {')': '(', '}': '{', ']': '['}  # 괄호 매핑
    opening_brackets = bracket_map.values()  # 여는 괄호들

    for char in expression:
        if char in opening_brackets:  # 여는 괄호가 나오면 스택에 추가
            stack.push(char)
        elif char in bracket_map.keys():  # 닫는 괄호가 나오면
            if stack.is_empty() or stack.pop() != bracket_map[char]:  # 스택이 비어있거나 짝이 맞지 않으면 False
                return False

    return stack.is_empty()  # 모든 괄호가 매칭되었는지 확인


# 사용 예시
if __name__ == "__main__":
    expressions = [
        "([]){}",   # True
        "{[()]}",   # True
        "((()))",   # True
        "({[})",    # False
        "({[}",     # False
        "([",       # False
        "({[}])"    # False
    ]

    for expr in expressions:
        print(f"{expr}: {is_balanced(expr)}")
