import time
from Utils.Vector import Vector
import uuid


class Particle:

    def __init__(self, pos, vel, next_pos_time, next_pos, max_vel, angle):
        self.id = uuid.uuid4()
        self.pos = pos
        self.vel = vel
        self.next_pos = next_pos
        self.next_pos_time = next_pos_time
        self.max_vel = max_vel
        self.angle = angle
        self.drawn = False
        self.current_time = time.time()

    def draw(self,  window):
        # ---------TESTING PURPOSES-----DO NOT REMOVE------
        # ratio = cam.dimCanv.copy().divide_vector(cam.dim)
        # self.radius*=ratio.get_x()
        # canvas.draw_circle(self.pos.getP(), self.radius, 1, 'White')
        # -------------------------------------------------

        distance = window.origin.copy().subtract(self.pos)
        if distance.get_x() < 0:
            distance.x *= -1
        if distance.get_y() < 0:
            distance.y *= -1
        if distance.get_x() < window.dim.get_x() / 2 and distance.get_y() < window.dim.get_y() / 2:
            # --------TESTING PURPOSES----DO NOT REMOVE-------------
            # cam.dim = Vector(2600*2, 1400*2)
            object_pos = self.pos.copy().transform_to_window(window)

            # 1cam.dim=Vector(1300,700)

        # DEVELOPER OPTION:
        # ----------------

    def bounce(self, normal):
        self.vel.reflect(normal)

    def move(self, pos):
        self.next_pos = pos
        self.time_to(self.max_vel)
        self.vel.negate()

    def update_pos_vel(self):
        if self.pos.copy().subtract(self.next_pos).dot(self.vel) > 0:
            self.vel.multiply(0)

        if self.pos != self.next_pos:
            x, y = self.pos.copy().distance_to_vector(self.next_pos)
            dist = Vector(x, y)
            dist.negate()

            if self.next_pos_time - time.time() <= 0:
                self.pos = self.next_pos
            else:
                self.vel = dist.divide(self.next_pos_time - time.time())
                self.vel.multiply(time.time() - self.current_time)
                self.pos.add(self.vel)

    def update(self):
        # if self.updateSprite:
        #     self.spriteSheet.update()
        if self.next_pos != self.pos:
            self.update_pos_vel()
        self.current_time = time.time()

    def time_to(self, max_vel):
        self.next_pos_time = time.time() + self.pos.copy().distance_to(self.next_pos) / max_vel
