##allows you to define custom behavior for operators in your classes.
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, vector):
            return vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, vector):
            return vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __repr__(self):
        return f"vector({self.x}, {self.y})"
v1 = vector(2, 3)
v2= vector(5, 7)
print(v1 + v2)  
print(v1 - v2)
print(v1 * 3)
print(v1==v2)
print(v1.__repr__())