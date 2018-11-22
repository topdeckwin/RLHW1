from transition import transition
from agent import agent
from actions import actions
from states import states
import numpy as np

env = states()
trans = transition()
robot = agent()
action = actions()

rewardCollection = []
for i in range(0,10000):
    # print "episode " + str(i)
    curReward = 0
    discount = 1
    for j in range(0, 10000):
        # print "move " + str(j)
        # robot.printLoc()
        destx, desty, reward = robot.uniformAction()
        curReward += reward * discount
        discount *= 0.9
        if destx == 4 and desty == 4:
            # print discount, curReward
            rewardCollection.append(curReward)
            robot.reset()
            break

arr = np.array(rewardCollection)
mean = np.mean(arr)
std = np.std(arr)
maximum = np.max(arr)
minimum = np.min(arr)
print mean, std, maximum, minimum

# same thing but with optimal policy
rewardCollection = []
for ii in range(0,10000):
    # print "episode " + str(i)
    curReward = 0
    discount = 1
    for jj in range(0, 10000):
        # print "move " + str(j)
        # robot.printLoc()
        destx, desty, reward = robot.optimalAction()
        curReward += reward * discount
        discount *= 0.9
        if destx == 4 and desty == 4:
            # print discount, curReward
            rewardCollection.append(curReward)
            robot.reset()
            break

arr = np.array(rewardCollection)
mean = np.mean(arr)
std = np.std(arr)
maximum = np.max(arr)
minimum = np.min(arr)
print mean, std, maximum, minimum


hit = 0
for iii in range(0,100000):
    # print "episode " + str(i)
    robot.setPos(4,3) # s8

    for jjj in range(0, 11):
        # print "move " + str(j)
        # robot.printLoc()
        destx, desty, reward = robot.uniformAction()

    if robot.x == 2 and robot.y == 4:
        hit+=1
print hit*1.0/100000
