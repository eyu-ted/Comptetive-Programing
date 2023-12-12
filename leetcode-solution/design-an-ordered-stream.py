class OrderedStream:

    def __init__(self, n: int):
        self.n=n
        self.p=0
        self.lis=[""]*n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lis[idKey-1]=value
        i=self.p
        while self.p<self.n and self.lis[self.p]!="":
            self.p+=1
        return self.lis[i:self.p] 
    





        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)