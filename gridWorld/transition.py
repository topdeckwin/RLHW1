import random
from states import states
import numpy as np

class transition:

    def __init__(self):
        pass

    @staticmethod
    def tryMove(x,y,a):
        a = np.random.choice([-1, (a+1)%4, (a-1)%4, a], 1, p=[0.1, 0.05, 0.05, 0.8])[0]
        if a not in [-1,0,1,2,3]:
            print "error"
        # rand = random.random()
        # if rand < 0.05:
        #     a = (a+4-1)%4
        # elif rand < 0.1:
        #     a = (a+1)%4
        # elif rand < 0.2:
        #     a = -1
        # print x,y,a
        destx, desty = transition.getDest(x,y,a)
        if not states.isLegal(destx, desty):
            destx, desty = (x,y)
        
        reward = 0
        if states.isWater(destx, desty):
            reward = -10
        elif states.isGoal(destx, desty):
            reward = 10
        # print x,y,a,destx,desty
        done = destx == 4 and desty == 4
        return destx, desty, reward, done

    @staticmethod
    def getDest(x,y,a):
        if a == -1:
            return x,y
        elif a == 0:
            return x+1,y
        elif a==1:
            return x,y-1
        elif a==2:
            return x-1,y
        elif a==3:
            return x,y+1
