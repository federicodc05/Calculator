import math


class calc:
    def __init__(self, x, y):
        self.sum = x + y
        self.diff = x - y
        self.prod = round(x * y, 2)
        if x == 0 and y == 0:
            self.power = math.nan
        else:
            self.power = x ** y
        if x == 0 and y == 0:
            self.div = math.nan
        if x != 0 and y == 0:
            self.div = math.inf
        if x != 0 and y != 0:
            self.div = round(x / y, 2)
        if y == 0:
            self.rt = math.inf
        if y != 0:
            self.rt = round(x ** (1/y), 2)


class trig:
    def __init__(self, x, i):
        if not i:
            self.cos = round(math.cos(x), 2)
            self.sin = round(math.sin(x), 2)
            self.tan = round(math.tan(x), 2)
        if i:
            self.cos = round(math.acos(x), 2)
            self.sin = round(math.asin(x), 2)
            self.tan = round(math.atan(x), 2)

    n = -3


class log:
    def __init__(self, x):
        global n
        if x > 0:
            self.log = round(math.log10(x), 2)
            self.In = round(math.log(x), 2)
            n = -3
        if x == 0:
            self.log = -math.inf
            self.In = -math.inf
            n = -1
        if x < 0:
            self.log = math.nan
            self.In = math.nan
            n = -1


class mod:
    def __init__(self, x, y):
        self.div = x // y
        self.mod = x % y


