class MinStack:
        def __init__(self):
            self.stack=[]
            self.minstack=[]

        def push(self, val):
            self.stack.append(val)
            if len(self.minstack)==0 or self.minstack[-1]>=val:
                self.minstack.append(val)
    
        def pop(self):
            x=self.stack.pop()
            if x==self.minstack[-1]:
                self.minstack.pop()

        def top(self):
            return self.stack[-1]
        
        def getMin(self):
            return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()