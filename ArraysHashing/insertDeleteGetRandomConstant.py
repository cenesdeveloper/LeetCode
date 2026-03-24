class RandomizedSet:

    def __init__(self):
        self.random = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val not in self.index:
            self.random.append(val)
            self.index[val] = len(self.random) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.index:
            old_index = self.index[val]
            last_index = len(self.random) - 1
            last_val = self.random[last_index]

            self.random[old_index] = last_val
            self.index[last_val] = old_index
            self.random.pop()
            del self.index[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.random)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()