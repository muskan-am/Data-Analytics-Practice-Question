
import math

class Cylinder:
    """Cylinder with radius r and height h."""
    def __init__(self, r, h):
        self.r = float(r)
        self.h = float(h)

    def csa(self):
        return 2 * math.pi * self.r * self.h

    def tsa(self):
        return 2 * math.pi * self.r * (self.r + self.h)

    def volume(self):
        return math.pi * self.r**2 * self.h


class Cone:
    """Right circular cone with radius r and height h."""
    def __init__(self, r, h):
        self.r = float(r)
        self.h = float(h)

    def slant_height(self):
        return math.sqrt(self.r**2 + self.h**2)

    def csa(self):
        l = self.slant_height()
        return math.pi * self.r * l

    def tsa(self):
        l = self.slant_height()
        return math.pi * self.r * (self.r + l)

    def volume(self):
        return (1/3) * math.pi * self.r**2 * self.h


class Cube:
    """Cube with side a.
    CSA treated as lateral surface area = 4 * a^2
    TSA = 6 * a^2
    """
    def __init__(self, a):
        self.a = float(a)

    def csa(self):
        return 4 * self.a**2  # lateral surface area

    def tsa(self):
        return 6 * self.a**2

    def volume(self):
        return self.a**3


class Cuboid:
    """Cuboid with length l, breadth b, height h.
    CSA treated as lateral surface area = 2*h*(l + b)
    """
    def __init__(self, l, b, h):
        self.l = float(l)
        self.b = float(b)
        self.h = float(h)

    def csa(self):
        return 2 * self.h * (self.l + self.b)

    def tsa(self):
        return 2 * (self.l*self.b + self.b*self.h + self.h*self.l)

    def volume(self):
        return self.l * self.b * self.h


class Sphere:
    """Sphere with radius r.
    CSA = TSA = 4 * pi * r^2
    """
    def __init__(self, r):
        self.r = float(r)

    def csa(self):
        return 4 * math.pi * self.r**2

    def tsa(self):
        return 4 * math.pi * self.r**2

    def volume(self):
        return (4/3) * math.pi * self.r**3
