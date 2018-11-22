import numpy as np
import random
import math

import gridWorld


class TD:

    def __init__(self, s0, max_step):
        self.s0 = s0
        self.s = s0
        self.max_step = max_step

    def setStep(self, f):
        self.step = f

    def resetState(self):
        self.s = self.s0

    def tabular(self, num_state):
        self.v = np.zeros(num_state)
        self.getV = lambda s: self.v[gridWorld.states.stateNum(s[0],s[1])]

        def f(self, s, v):
            self.v[gridWorld.states.stateNum(s[0], s[1])] = v

        self.setV = f

    def fouriour(self, order):


    def run(self, policy, alpha, gamma, num_episode):
        mstde = []
        for i in range(num_episode):
            done = False
            self.resetState()
            for j in range(self.max_step):
                if done: break

                a = policy()
                s_new, r, done = self.step(self.s, a)

                tderror = r+gamma*self.getV(s_new)-self.getV(self.s)
                if (i < 100):
                    self.setV(self, self.s, self.getV(self.s) + alpha*tderror)
                else:
                    mstde.append(tderror**2)
                self.s = s_new
        return sum(mstde)/len(mstde)





def main():
    tdGrid()


def tdGrid():
    alphas = [0.1, 0.01, 0.001]
    y = []
    grid = TD((0, 0), 40)
    grid.tabular(23)

    def gridstep(s, a):
        x, y, r, d = gridWorld.transition.tryMove(s[0], s[1], a)
        xy = (x, y)
        return xy, r, d

    grid.setStep(gridstep)
    for alpha in alphas:
        temp = grid.run(lambda: math.floor(random.random() * 4),
                        alpha, 0.9, 110)
        y.append(temp)
