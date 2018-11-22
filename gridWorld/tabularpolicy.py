import numpy as np
from transition import transition as t
from states import states


class TabularPolicy():

    def __init__(self):
        self.policy = np.zeros(23*4)
        self.cache = {}

    @staticmethod
    def softmax(x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    def getAction(self, x, y):
        n = states.stateNum(x,y)
        # if self.cache.has_key(n):
        #     return np.random.choice(4,1,p=self.cache[n])[0]
        # else:
        sftmx = TabularPolicy.softmax(self.policy.reshape((23,4))[n-1])
        # self.cache[n] = sftmx
        res = np.random.choice(4,1,p=sftmx)[0]
        return res

    def run(self):
        done = False
        x=0
        y=0
        discount = 1
        curReward = 0
        T = []
        for i in range(45):
            if done or curReward < 0:
                break
            n = states.stateNum(x, y)
            T.append(n)
            a = self.getAction(x,y)
            destx, desty, reward, done = t.tryMove(x,y,a)
            curReward += reward * discount
            discount *= 0.9
            x = destx
            y = desty
        # print T
        return curReward

    def sample(self, mean, cov):
        self.policy = np.random.multivariate_normal(mean, cov, 1)[0]
        # self.policy /= np.linalg.norm(self.policy)
        self.clean()
        return self.policy

    def set(self, p):
        self.policy = p
        self.clean()

    def sample_mean(self):
        return np.random.rand(self.policy.shape[0])
        # ret = np.array([1,2,3,4]*23)
        # np.random.shuffle(ret)
        # return ret

    def clean(self):
        self.cache = {}


