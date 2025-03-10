class RandomizedSet:

    def __init__(self):
        self.indx = 0
        self.list = []
        self.dictionary = {}

    def insert(self, val: int) -> bool:
        if val not in self.dictionary:
            self.list.append(val)
            self.dictionary[val] = self.indx
            self.indx += 1
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.dictionary:
            pop = self.list[-1]
            i = self.dictionary[val]
            self.list[i] = pop
            self.dictionary[pop] = i
            self.list.pop()
            del self.dictionary[val]
            self.indx -= 1
            return True
        return False

    def getRandom(self) -> int:

        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()