import math

class Tuple(object):
    """A simple 4 dimensional tuple object that contains an x, y, and z component along with a weight (w)
    """
    
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        
    def is_point(self):
        return self.w == 1

    def is_vector(self):
        return self.w == 0

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

    def normalize(self):
        magnitude = self.magnitude()
        return Tuple(self.x / magnitude, self.y/magnitude, self.z/magnitude, self.w/magnitude)

    def dot(self, o):
        return self.x * o.x + self.y * o.y + self.z * o.z + self.w * o.w

    def cross(self, o):
        return Vector(self.y * o.z - self.z * o.y,
                      self.z * o.x - self.x * o.z,
                      self.x * o.y - self.y * o.x)

    def __add__(self, o):
        w = self.w + o.w
        if w == 1:
            return Point(self.x + o.x, self.y + o.y, self.z + o.z)
        elif w == 0:
            return Vector(self.x + o.x, self.y + o.y, self.z + o.z)
        else:
            return Tuple(self.x + o.x, self.y + o.y, self.z + o.z, w)

    def __sub__(self, o):
        w = self.w - o.w
        if w == 1:
            return Point(self.x - o.x, self.y - o.y, self.z - o.z)
        elif w == 0:
            return Vector(self.x - o.x, self.y - o.y, self.z - o.z)
        else:
            raise TypeError("Incompatible tuple subtraction")

    def __mul__(self, o):
        _type = type(o)
        if _type is int or _type is float:
            return Tuple(self.x*o, self.y*o, self.z*o, self.w*o)
        else:
            raise TypeError("Invalid tuple multiplication")

    def __truediv__(self, o):
        _type = type(o)
        if _type is int or _type is float:
            return Tuple(self.x/o, self.y/o, self.z/o, self.w/o)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y and self.z == o.z and self.w == o.w

    def __neg__(self):
        w = -self.w
        if w == 1:
            return Point(-self.x, -self.y, -self.z)
        elif w == 0:
            return Vector(-self.x, -self.y, -self.z)
        else:
            return Tuple(-self.x, -self.y, -self.z, w)

class Point(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1)

class Vector(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0)

class Color(Tuple):
    def __init__(self, x, y, z, w=1):
        super().__init__(x, y, z, w)
    
    @property
    def red(self):
        return self.x

    @red.setter
    def red(self, value):
        self.x = value

    @property
    def green(self):
        return self.y

    @green.setter
    def green(self, value):
        self.y = value

    @property
    def blue(self):
        return self.z

    @blue.setter
    def blue(self, value):
        self.z = value

    @property
    def alpha(self):
        return self.w

    @alpha.setter
    def alpha(self, value):
        self.w = value

    def norm_convert_255(self):
        if self.red > 1:
            red = 255
        elif self.red < 0:
            red = 0
        else:
            red = self.red * 255

        if self.green > 1:
            green = 255
        elif self.green < 0:
            green = 0
        else:
            green = self.green * 255

        if self.blue > 1:
            blue = 255
        elif self.blue < 0:
            blue = 0
        else:
            blue = self.blue * 255

        return (round(red), round(green), round(blue))

    def __add__(self, o):
        return Tuple(self.x + o.x, self.y + o.y, self.z + o.z, self.w + o.w)

    def __sub__(self, o):
        return Tuple(self.x - o.x, self.y - o.y, self.z - o.z, self.w - o.w)

    def __mul__(self, o):
        _type = type(o)
        if _type is int or _type is float:
            return Tuple(self.x*o, self.y*o, self.z*o, self.w*o)
        if _type is Color:
            return Color(self.red * o.red, self.green * o.green,
                         self.blue * o.blue, self.alpha * o.alpha)
