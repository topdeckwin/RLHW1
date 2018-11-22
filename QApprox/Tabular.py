
class Tabular:

    def __init__(self, sizeS, sizeA):
        self.values = [[] for _ in range(sizeS)]
        for x in self.values:
            x = [0 for _ in range(sizeA)]

    def __getitem__(self, item1, item2):
        return self.values[item1][item2]

    def getBestAction(self, s):
        qs = self.values[s]
        maxQ = 0
        maxA = 0
        for i, q in enumerate(qs):
            if(q > maxQ):
                maxQ = q
                maxA = i
        return maxA
