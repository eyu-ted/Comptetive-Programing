class Bitset:

    def __init__(self, size: int):
        self.set=[0]*size
        self.size=size
        self.count1=0
        self.flipped=False

        

    def fix(self, idx: int) -> None:
        if self.flipped and self.set[idx]:
            self.set[idx]=0
            self.count1+=1
        elif not self.set[idx] and not self.flipped:
            self.set[idx]=1
            self.count1+=1

    def unfix(self, idx: int) -> None:
        if self.flipped and not self.set[idx]:
            self.set[idx]=1
            self.count1-=1
        elif self.set[idx] and not self.flipped:
            self.set[idx]=0
            self.count1-=1

        

    def flip(self) -> None:
        self.flipped=not self.flipped
        self.count1=self.size-self.count1

    def all(self) -> bool:
        return self.size==self.count1
        

    def one(self) -> bool:
        return self.count1>0

    def count(self) -> int:
        return self.count1
        

    def toString(self) -> str:
        if self.flipped:
            return "".join("0" if i else "1" for i in self.set)
        return "".join("1" if i else "0" for i in self.set)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()