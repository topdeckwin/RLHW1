import numpy as np
from crossentrophy import CrossEntropy
from fchc import FCHC
from gridWorld.tabularpolicy import TabularPolicy
import matplotlib.pyplot as plt
from cartPole.linearpolicy import LinearPolicy
import random

def plot(all_G, name):
    x = range(0,len(all_G[0]))
    temp = plt.figure()
    Gs = np.array(all_G)
    avg = np.average(Gs, axis=0)
    std = np.std(Gs, axis=0)
    plt.xlim(0, x[-1]+1)
    plt.errorbar(x, avg, yerr=std, ecolor='g')
    plt.show()
    temp.savefig(name)

def hyper_search_CE(policy):
    p = policy()
    time = 10000000
    J = -100000
    best_trail = 0
    for i in range(200):
        if i%10 == 0:
            print "trail " + str(i)

        mean = p.sample_mean()
        np.random.shuffle(mean)
        K = random.randrange(10,50,2)
        Ke = random.randrange(1,K,1)
        # Ke = K/2
        N = random.randrange(1,21,2)
        epsilon = pow(0.1, random.randrange(2,10,2))
        cov = np.eye(mean.shape[0])*random.random()*2
        print K, Ke, N
        _, new_time, new_J = CrossEntropy.run(p, mean, cov, K, Ke, N, epsilon)
        if new_J > J:
            J = new_J
            best_mean = mean
            best_cov = cov[0][0]
            best_K = K
            best_Ke = Ke
            best_N = N
            best_e = epsilon
            best_trail = i
            time = new_time
            print new_J
    f = open(str(policy) + "-CE.txt", "w")
    f.writelines(str(x) + "\n" for x in [time, J, best_mean, best_cov, best_K, best_Ke, best_N, best_e])
    f.flush()
    f.close()

def grid_CE():
    mean = np.array([.60, .22, .05,  .04, .77, .94, .52, .46, .84, .67, .39, .95, .48, .84, .28, .88, .79, .67, .70, .98,
                     .78, .13,  .00, .44, .38, .52, .74, .40, .77, .40, .74, .64, .75, .44, .47, .63, .25, .23, .04, .78,
                     .90, .87, .25, .68, .58, .85,  .02, .94, .87, .97, .78, .56, .24, .20,  .07, .51, .80, .20, .70, .01,
                     .51, .59, .18, .22, .64, .53, .74, .13,  .09, .55, .60, .92, .13, .15, .59, .47, .18, .89, .58,  .03,
                     .37, .52, .40, .33, .53, .23, .12,  .75, .52,  .02, .48, .34])

    cov = np.eye(mean.shape[0]) * 0.05841941
    K = 30
    Ke = 3
    N = 10
    epsilon = 0.001
    all_G = []
    for i in range(500):
        print i
        Gs, _, _ = CrossEntropy.run(TabularPolicy(), mean, cov, K, Ke, N, epsilon)
        all_G.append(Gs)
        if i % 5 == 0:
            plot(all_G, "grid-CE"+str(i))


def cartpole_CE():
    # mean = np.array([-26.15070606, -25.76598276,
    #                  13.07125472, 39.79620511,
    #                  -9.9010186,   34.01682909,
    #                  -6.88827136,  75.8728528,
    #                  22.28093349,  24.07786972])
    mean = np.array([ 0.67599725,  0.39822786,
                      0.83334446,  0.7874999,
                      0.25195655,  0.81885796,
                      0.66581799,  0.96591531,
                      0.24764307,  0.32707893])
    cov = np.eye(mean.shape[0]) * 1.33106675304
    K = 46
    Ke = 3
    N = 7
    epsilon = 0.01
    all_G = []
    for i in range(500):
        print i
        Gs, _, _ = CrossEntropy.run(LinearPolicy(), mean, cov, K, Ke, N, epsilon, 20)
        all_G.append(Gs)
        if i % 1 == 0:
            plot(all_G, "cartpole-CE"+str(i))

def hyper_search_FCHC(policy):
    p = policy()
    time = 10000000
    J = -100000
    best_trail = 0
    for i in range(100):
        if i%10 == 0:
            print "trail " + str(i)

        mean = p.sample_mean()
        np.random.shuffle(mean)
        exp = random.random()
        N = random.randrange(2,20,1)
        _, _, new_J = FCHC.run(p, mean, exp, N)
        print new_J
        if new_J > J:
            J = new_J
            best_mean = mean
            best_N = N
            best_exp = exp
            best_trail = i
            print new_J
    f = open(str(policy) + "-FCHC.txt", "w")
    f.writelines(str(x) + "\n" for x in [time, J, best_mean, best_N, best_exp])
    f.flush()
    f.close()

def cartpole_FCHC():
    all_G = []
    for i in range(500):
        mean = np.array([32.71583166,  25.35004176,  50.7846944,   74.5123285 ,  46.2971819,
         33.39312313,  47.09876731,  47.67445611,  72.85090019,  78.58948496])
        N = 16
        exp = 70.2493043236
        print i
        Gs, _, _ = FCHC.run(LinearPolicy(), mean, exp, N)
        all_G.append(Gs)
        if i % 10 == 0:
            plot(all_G, "cartpole-FCHC")

def grid_FCHC():
    all_G = []
    for i in range(500):
        mean = np.array([76.32264034, 88.85438911, 25.37159214, 53.31848954, 23.60454635
        , 32.66080321, 4.64103002, 90.48749164, 87.29867988, 54.24287737
        , 60.00989981, 41.9451613, 75.28802564, 72.53053103, 34.52707346
        , 67.65490957, 0.6543433, 72.47199775, 50.36838004, 61.52147653
        , 15.64405038, 92.08297684, 22.33220262, 75.36172566, 99.52824153
        , 73.5318653, 75.95226757, 65.654366, 62.14376554, 10.5520761
        , 65.7399387, 54.52815304, 12.63656016, 70.58144049, 16.31201271
        , 4.66064164, 32.90372229, 54.40406378, 46.33262108, 95.02222205
        , 52.48591017, 77.18626484, 77.77305816, 32.0154614, 0.26450878
        , 46.14006471, 38.12369834, 74.80265174, 62.26272586, 13.59052483
        , 68.43994343, 9.12184167, 28.00439575, 48.43989843, 49.07652863
        , 86.78145248, 97.15832082, 1.84053975, 66.37286468, 84.26058185
        , 48.81276777, 92.51192811, 86.22542622, 67.09445506, 7.47730002
        , 82.68822903, 63.10100388, 49.54332037, 5.95579119, 11.96663117
        , 17.11598911, 16.2424487, 79.65136626, 45.83666597, 2.35267371
        , 39.12228307, 22.28325391, 48.62815733, 37.38375717, 77.72435213
        , 52.76075095, 62.38869404, 29.01956024, 51.40564962, 94.01243391
        , 57.08799026, 67.27276965, 41.13144044, 23.77289398, 30.08955979
        , 57.82416866, 69.66716741])
        N = 17
        exp = 82.4936332007
        print i
        Gs, _, _ = FCHC.run(TabularPolicy(), mean, exp, N)
        all_G.append(Gs)
        if i % 2 == 0:
            plot(all_G, "grid-FCHC")

if __name__ == '__main__':
    # hyper_search_FCHC(TabularPolicy)
    # hyper_search_FCHC(LinearPolicy)
    # hyper_search_CE(TabularPolicy)
    # hyper_search_CE(LinearPolicy)
    # grid_FCHC()
    # cartpole_FCHC()
    cartpole_CE()
    # grid_CE()


