# https://leetcode.com/problems/map-sum-pairs/



class MapSum:

    def __init__(self):
        self.dict = defaultdict(int)        # map prefix to sum of vals with that prefix
        self.words = defaultdict(int)       # map whole words to their val

    def insert(self, key, val):
        if key in self.words:               # update words and update val to change in val
            self.words[key], val = val, val - self.words[key]
        else:
            self.words[key] = val           # insert into words

        for i in range(len(key)):
            prefix = key[:i + 1]
            self.dict[prefix] += val        # update dict for all prefixes

    def sum(self, prefix):
        return self.dict[prefix]
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
