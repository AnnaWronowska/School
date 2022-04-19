import math


def sqrroot(a):
    if a == 0:
        return a
    x0 = a / 2
    x1 = a / x0
    limit = 30
    while math.fabs(x0 - x1) > 0.000000000000001 and limit > 0:
        x0 = (x0 + x1) / 2
        x1 = a / x0
        limit -= 1
    return x1


def cuberoot(a):
    if a == 0:
        return a
    x0 = a / 2
    x1 = a / (x0 ** 2)
    limit = 30
    while math.fabs(x0 - x1) > 0.00000000000001 and limit > 0:
        x0 = (x0 + x1) / 2
        x1 = a / (x0 ** 2)
        limit -= 1
    return x1


def discretionaryroot(a, n):
    if a == 0 or n == 1:
        return a
    if n == 0:
        return 1
    x0 = a / 2
    x1 = a / (x0 ** (n - 1))
    limit = 50
    while math.fabs(x0 - x1) > 0.00000000000001 and limit > 0:
        x0 = (x0 + x1) / 2
        x1 = a / (x0 ** (n - 1))
        limit -= 1
    return x1


#for i in range(0, 101):
#    print(sqrroot(i))
#for i in range(0, 101):
#    print(cuberoot(i))
print(discretionaryroot(16, 4))
