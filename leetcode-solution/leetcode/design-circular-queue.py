class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.length=0
        self.queue=[]
        

    def enQueue(self, value: int) -> bool:
        if self.k>len(self.queue):
            temp=[value]

            for n in self.queue:
                temp.append(n)
            
            self.queue=temp
            self.length+=1
            return True


        return False
        
        
        
            

    def deQueue(self) -> bool:
        if self.queue :
            self.queue.pop()
            self.length -= 1
            return True
        return False
        


        

    def Front(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1
        

    def Rear(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1
        

    def isEmpty(self) -> bool:
        if self.queue:
            return False
        return True
        

    def isFull(self) -> bool:
        if self.k == len(self.queue):
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()