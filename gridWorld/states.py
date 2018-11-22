

class states:

    def __init__(self):
        self.states = [(j,i) for i in range(0,5) for j in range (0,5)]

    @staticmethod
    def isObstacle(x,y):
        return x == 2 and (y == 2 or y == 3)

    @staticmethod    
    def isOutside(x,y):
        return x < 0 or y < 0 or x > 4 or y > 4

    @staticmethod
    def isLegal(x,y):
        return not states.isObstacle(x,y) and not states.isOutside(x,y)
    
    @staticmethod
    def isWater(x,y):
        return x == 2 and y == 4

    @staticmethod   
    def isGoal(x,y):
        return x == 4 and y == 4

    @staticmethod
    def stateNum(x,y):
        n = y*5+x+1
        if n >= 14:
            n-=1
        if n >=18:
            n-=1
        return n

    
    
    

if __name__ == "__main__":
    a = states()
    print a.states, states.isLegal(0,0)
