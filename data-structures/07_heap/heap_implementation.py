class Heap:
    def __init__(self) -> None:
        self.heap = [0]

    def push(self,data):
        self.heap.append(data)
        i = len(self.heap) - 1

        #percolate up
        while self.heap[i] < self.heap[i//2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = temp
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        #move last value to root
        self.heap[1]  = self.heap.pop()
        i = 1

        #percolate down
        while 2 * i < len(self.heap):
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[2 * i + 1] < self.heap[i]:
                #swap right child
                temp = self.heap[2 * i + 1]
                self.heap[2 * + 1] = self.heap[i]
                self.heap[i] = temp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                #swap left child
                temp = self.heap[2 * i]
                self.heap[2 * i] = self.heap[i]
                self.heap[i] = temp
                i = 2 * i
            else:
                break
        
        return res
    
h = Heap()
h.push(3)
h.push(5)
h.push(32)
h.push(2)
h.pop()
print(h.heap)