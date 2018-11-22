from state import State
import config as c
import math as m

class Transition:

    def __init__(self):
        pass

    @staticmethod
    def step(s, action):

        f = c.motor_force if action == 1 else -c.motor_force
        x = s.getPosition()
        theta = s.getAngle()
        theta_dot = s.getAngularVelocity()

        sin = m.sin(theta)
        cos = m.cos(theta)

        mass = c.pole_mass + c.cart_mass

        new_theta_acc = (c.g * sin + cos * (-f - c.pole_mass * c.pole_half_length * theta_dot * theta_dot * sin)
                     / (mass)) / (c.pole_half_length * (4 / 3 - (c.pole_mass * cos * cos) / (mass)))
        new_x_acc = (f + c.pole_mass * c.pole_half_length * (theta_dot ** 2 * sin - new_theta_acc * cos))\
                    / (mass)
        new_v = s.getVelocity() + c.delta_t *new_x_acc
        new_x = x + c.delta_t * s.getVelocity()
        new_theta_dot = theta_dot + c.delta_t*new_theta_acc
        new_theta = theta + c.delta_t * theta_dot
        new_t = s.getTime() + c.delta_t

        done = abs(new_x) > c.fail_x or abs(new_theta) > c.fail_angle or new_t > c.max_t or abs(new_v) > 10\
               or abs(new_theta_dot) > m.pi
        reward = 0 if done else 1

        new_s = State()
        new_s.pos = new_x
        new_s.v = new_v
        new_s.angle = new_theta
        new_s.angular_v = new_theta_dot
        new_s.time = new_t

        return new_s, reward, done