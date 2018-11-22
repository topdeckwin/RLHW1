import config


class State:

    def __init__(self):
        self.reset()

    def reset(self):
        self.pos = 0.0
        self.v = 0.0
        self.angle = 0.0
        self.angular_v = 0.0
        self.time = 0.0

    def increaseT(self):
        self.time +=config.delta_t

    def getAngle(self):
        return self.angle

    def getVelocity(self):
        return self.v

    def getAngularVelocity(self):
        return self.angular_v

    def getPosition(self):
        return self.pos

    def getTime(self):
        return self.time

