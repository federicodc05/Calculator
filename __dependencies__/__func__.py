import math


def exp(a, z, n):
    e = round(math.exp(a), 2)
    z.configure(text=e)
    n = -3
    dec = True
    return e


def root(a, z, n):
    if a < 0:
        e = math.nan
    else:
        e = round(math.sqrt(a), 2)
    z.configure(text=e)
    n = -3
    return e


def log10(a, z, n):
    if a > 0:
        e = round(math.log10(a), 2)
    if a == 0:
        e = -math.inf
    if a < 0:
        e = math.nan
    z.configure(text=e)
    n = -3
    return e


def nat_log(a, z, n):
    if a > 0:
        e = round(math.log(a), 2)
    if a == 0:
        e = -math.inf
    if a < 0:
        e = math.nan
    z.configure(text=e)
    n = -3
    return e


def erf(a, z, n):
    e = round(math.erf(a), 2)
    z.configure(text=e)
    n = -3
    return e


def gamma(a, z, n):
    e = round(math.gamma(a), 2)
    z.configure(text=e)
    n = -3
    return e
