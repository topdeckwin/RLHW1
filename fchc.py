import numpy as np


class FCHC:

    def __init__(self):
        pass

    @staticmethod
    def run(policy, mean, exp, N):
        history = []
        policy.set(mean)
        J_hat, _ = FCHC.evaluate(policy, N)
        theta = mean
        cov = np.eye(mean.size)*exp
        for i in range(300):
            # print i
            new_theta = policy.sample(theta, cov)
            new_J, new_G = FCHC.evaluate(policy,N)
            history.extend(new_G)
            if new_J > J_hat:
                theta = new_theta
                J_hat = new_J
        return  history, 0, J_hat


    @staticmethod
    def evaluate(policy, N):
        Gs = []
        J = 0.0
        for i in range(N):
            temp = policy.run()
            Gs.append(temp)
            J += temp
        return J/N, Gs