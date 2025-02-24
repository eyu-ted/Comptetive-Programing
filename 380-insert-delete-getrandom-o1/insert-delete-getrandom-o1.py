class RandomizedSet:

    def __init__(self):
        self.dictionary = {}
        self.lis = []
        

    def insert(self, val: int) -> bool:
        if val in self.dictionary:
            return False

        self.dictionary[val] = len(self.lis)
        self.lis.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dictionary:
            return False
        
        index = self.dictionary[val]
        self.lis[index] = self.lis[-1]
        self.dictionary[self.lis[-1]] = index

        self.lis.pop()
        self.dictionary.pop(val)

        return True
        

    def getRandom(self) -> int:
        return choice(self.lis)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()