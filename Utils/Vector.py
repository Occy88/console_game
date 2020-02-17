import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def negate(self):
        self.multiply(-1)

    def getP(self):
        return (self.x, self.y)

    def set(self,vector):
        self.x=vector.x
        self.y=vector.y
    def copy(self):
        v = Vector(self.x, self.y)
        return v

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def multiply(self, k):
        self.x *= k
        self.y *= k
        return self

    def multiply_vector(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def divide(self, k):
        self.x /= k
        self.y /= k
        return self

    def divide_vector(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def normalize(self):
        return self.divide(self.length())

    def isEqual(self, other):
        return self.x == other.x and self.y == other.y

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Returns the length of the vector
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def size(self):
        return self.x + self.y

    # Returns the squared length of the vector
    def lengthSq(self):
        return self.x ** 2 + self.y ** 2

    def distance_to(self, pos):
        return math.sqrt((self.x - pos.x) ** 2 + (self.y - pos.y) ** 2)

    def distance_to_vector(self, pos):
        return self.x - pos.x, self.y - pos.y

    # Reflect this vector on a normal
    def reflect(self, normal):
        n = normal.copy()
        n.mult(2 * self.dot(normal))
        self.subtract(n)
        return self

    def rotate(self, angle):
        self.x = self.x * math.cos(angle) - self.y * math.sin(angle)
        self.y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return self

    def get_angle(self, other):
        return math.acos(self.dot(other))

