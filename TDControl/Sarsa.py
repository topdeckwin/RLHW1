
class Sarsa:

    def __init__(self, fa, env):
        self.fa = fa
        self.env = env

    def run(self, episodes):
        for i in range(episodes):
            s = self.env.d0()



