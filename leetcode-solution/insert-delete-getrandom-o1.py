import random

class RandomizedSet:
    def __init__(self):
        self.value_to_index = {}
        self.values = []

    def insert(self, val):
        if val in self.value_to_index:
            return False 

        self.values.append(val)
        self.value_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val):
        if val not in self.value_to_index:
            return False 

        last_value = self.values[-1]
        index = self.value_to_index[val]
        self.values[index] = last_value
        self.value_to_index[last_value] = index
        self.values.pop()
        del self.value_to_index[val]

        return True

    def getRandom(self):
        random_index = random.randint(0, len(self.values) - 1)
        return self.values[random_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()