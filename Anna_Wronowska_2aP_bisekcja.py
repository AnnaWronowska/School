# POPRAWIĆ BO GÓWNO NIE DZIAŁA
# ZWŁASZCZA ZERO OF A FUNCTION, TO MOŻE BYĆ ŹRÓDŁO PROBLEMU

import math

precX = 0.0000000001
prec0 = 0.0000000001
step = 0.001


def zero_of_a_function(pleft, pright, degree, factors):
    fleft = horner(degree, pleft, factors)
    fright = horner(degree, pright, factors)
    while math.fabs(pleft - pright) > precX:
        x1 = (pleft + pright) / 2
        f1 = horner(degree, x1, factors)
        if math.fabs(f1) < prec0:
            return x1
        if fleft * f1 < 0:
            pright = x1
        else:
            pleft = x1



def horner(n, x, list1):
    list2 = [list1[0]]
    for i in range(1, n + 1):
        list2.append(list2[i - 1] * x + list1[i])
    return list2[n]


def bisection_horner(left, right, degree, factors):
    x = left
    while x < right:
        if horner(degree, x, factors) * horner(degree, x + step, factors) < 0:
            print(zero_of_a_function(x, x + step, degree, factors))


left = int(input('Podaj lewy kraniec zakresu x-ów\n'))
right = int(input('Podaj prawy kraniec zakresu x-ów\n'))
degree = int(input('Podaj stopień wielomianu\n'))
factors = []
for i in range(degree + 1):
    factors.append(int(input('Podaj współczynnik wielomianu przy x^' + f'{degree - i}' + '\n')))
bisection_horner(left, right, degree, factors)
