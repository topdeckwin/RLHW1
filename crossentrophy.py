import numpy as np
import time

class CrossEntropy():

    def __init__(self):
        pass

    @staticmethod
    def run(policy, mean, cov, K, Ke, N, epsilon, outer_episodes):
        now = time.time()
        history = []
        J = 0
        for i in range(outer_episodes):
            # if i == 299:
            #     print "out of time!"
            mean, cov, new_J, Gs = CrossEntropy.run_helper(policy, mean, cov, K, Ke, N, epsilon)
            history.extend(Gs)
            # print len(Gs)
            # if new_J-J < 0.0000000000001:
            #     return Gs, time.time() - now, new_J
            # else:
            #     J = new_J
        return history, time.time() - now, new_J

    @staticmethod
    def run_helper(policy, mean, cov, K, Ke, N, epsilon):
        # print cov.shape
        # mean /= np.linalg.norm(mean)
        history = []
        G = []
        for i in range(K):
            cur_policy = policy.sample(mean, cov)
            # print mean, cur_policy
            J = 0.0
            for j in range(N):
                cur_J = policy.run()
                G.append(cur_J)
                J += cur_J
            J = J/N
            history.append((cur_policy, J))
        history = sorted(history, key=lambda x: x[1])
        history.reverse()
        print [x[1] for x in history]
        theta = history[0][0]
        new_mean = theta
        J = 0
        for i in range(1, Ke) :
            J += history[i][1]
            new_mean += theta
        new_mean /= Ke

        theta = history[0][0]
        new_cov = np.outer((theta - new_mean), (theta - new_mean))
        for i in range(1, Ke):
            theta = history[i][0]
            new_cov += np.outer((theta - new_mean),(theta - new_mean))
        # print theta
        new_cov = (new_cov /(epsilon+Ke))+ (np.eye(new_mean.size)*epsilon)/(epsilon+Ke)
        return new_mean, new_cov, J / Ke, G





