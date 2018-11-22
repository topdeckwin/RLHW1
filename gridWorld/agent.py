import random
from transition import transition

class agent():

    def __init__(self):
        self.reset()
    
    def reset(self):
        self.setPos(0,0)

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def printLoc(self):
        print str(self.x) + " " + str(self.y)
    
    def uniformAction(self):
        action = random.randint(0, 3)
        destx, desty, reward = transition.tryMove(self.x, self.y, action)
        self.x, self.y = destx, desty
        return destx, desty, reward

    def optimalAction(self):
        optimalAction = [
            [0,0,0,0,3],
            [0,0,0,0,3],
            [1,1,-1,3,3],
            [1,1,-1,3,3],
            [1,2,0,0,-1]
        ]
        action = optimalAction[self.y][self.x]
        destx, desty, reward = transition.tryMove(self.x, self.y, action)
        self.x, self.y = destx, desty
        return destx, desty, reward