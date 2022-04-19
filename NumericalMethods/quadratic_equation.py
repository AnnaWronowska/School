import math


def quadraticdelta(i, j, k):
    delta = j * j - 4 * i * k
    if delta < 0:
        return 'brak miejsc zerowych'
    elif delta == 0:
        x = (- j) / 2 * i
        return x
    x1 = ((- j) - math.sqrt(delta)) / 2 * i
    x2 = ((- j) + math.sqrt(delta)) / 2 * i
    return (x1, x2)


print(quadraticdelta(1, 4, 3))
