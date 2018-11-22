import numpy as np
from state import State
from transition import Transition


class LinearPolicy():

    def __init__(self):
        self.policy = np.zeros(10)

    @staticmethod
    def softmax(x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    def getAction(self, s):
        s_v = np.array([s.getPosition(), s.getVelocity(), s.getAngle(), s.getAngularVelocity()])
        W = self.policy[0:8].reshape(4, 2)
        b = self.policy[8:]
        prob = LinearPolicy.softmax(s_v.dot(W) + b)
        res = np.random.choice(2, 1, p=prob)[0]
        return res

    def run(self):
        done = False
        s = State()
        G = 0
        while not done:
            a = self.getAction(s)
            new_s, reward, done = Transition.step(s, a)
            G+=reward
            s = new_s
        return G

    def sample(self, mean, cov):
        self.policy = np.random.multivariate_normal(mean, cov, 1)[0]
        # self.policy /= np.linalg.norm(self.policy)
        return self.policy

    def set(self, p):
        self.policy = p

    def sample_mean(self):
        return np.random.rand(self.policy.shape[0])