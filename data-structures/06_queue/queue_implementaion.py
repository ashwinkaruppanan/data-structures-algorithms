from collections import deque

class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self,data):
        self.queue.appendleft(data)

    def dequeue(self):
        return self.queue.pop()
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.queue)
