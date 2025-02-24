class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.Circular = deque()
        self.count = 0
        

    def enQueue(self, value: int) -> bool:
        if self.count < self.length:
            self.Circular.append(value)
            self.count += 1 
            return True
        return False
        
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.Circular.popleft()
            self.count -= 1
            return True
        return False
        

    def Front(self) -> int:
        if self.isEmpty() :
            return -1
        return self.Circular[0]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.Circular[-1]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.length
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()