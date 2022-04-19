from math import pi, sin

step = 0.0001


def rectangle_integral(left, right, function):
    result = 0
    i = left
    while i + step <= right:
        result += function((i + i + step) / 2) * step
        i += step
    return result


def trapezium_integral(left, right, function):
    result = 0
    i = left
    while i + step <= right:
        result += (function(i) + function(i + step)) * step / 2
        i += step
    return result


def rectangle_integral_horner(left, right, n, list1):
    result = 0
    i = left
    while i + step <= right:
        result += horner(n, (i + i + step) / 2, list1) * step
        i += step
    return result


def trapezium_integral_horner(left, right, n, list1):
    result = 0
    i = left
    while i + step <= right:
        result += (horner(n, i, list1) + horner(n, i + step, list1)) * step / 2
        i += step
    return result


def horner(n, x, list1):
    list2 = [list1[0]]
    for i in range(1, n + 1):
        list2.append(list2[i - 1] * x + list1[i])
    return list2[n]


# f(x) = sin(x) dla <0; pi>
# g(x) = x^7 - 3x^6 - 4x^5 + 12x^4 - x^3 + 3x^2 + 4x + 12 dla <-1; 1>
# h(x) = x^3 - x^2 - 4x + 4 dla <-2; 2>
g = [1, -3, -4, 12, -1, 3, 4, -12]
h = [1, -1, -4, 4]
print('Całka f(x) metodą prostokątów: ' + f'{rectangle_integral(0, pi, sin)}')
print('Całka f(x) metodą trapezów: ' + f'{trapezium_integral(0, pi, sin)}')
print('Całka g(x) metodą prostokątów: ' + f'{rectangle_integral_horner(-1, 1, 7, g)}')
print('Całka g(x) metodą trapezów: ' + f'{trapezium_integral_horner(-1, 1, 7, g)}')
print('Całka h(x) metodą prostokątów: ' + f'{rectangle_integral_horner(-2, 2, 3, h)}')
print('Całka h(x) metodą trapezów: ' + f'{trapezium_integral_horner(-2, 2, 3, h)}')
