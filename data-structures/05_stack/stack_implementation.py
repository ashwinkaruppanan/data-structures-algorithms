from collections import deque

class Stack:
    def __init__(self) -> None:
        self.stack = deque()

    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(1)
s.push(2)
s.push(3)
print(s.stack)
# print(s.peek())
# print(s.is_empty())
# print(s.size())