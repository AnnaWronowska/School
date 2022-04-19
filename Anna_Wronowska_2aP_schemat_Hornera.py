def horner_ite(n: int, x, list1: list):
    list2 = [list1[0]]
    for i in range(1, n + 1):
        list2.append(list2[i - 1] * x + list1[i])
    return list2[n]


def horner_rec(n: int, x, list1: list):
    if n == 0:
        return list1[0]
    return horner_rec(n - 1, x, list1) * x + list1[n]


if __name__ == "__main__":
    n0 = int(input('Podaj stopien wielomianu\n'))
    list0 = []
    print('Podaj kolejne wspolczynniki wielomianu')
    for i in range(n0 + 1):
        list0.append(int(input()))
    x0 = int(input('Podaj wartosc x\n'))
    print('Horner iteracyjnie: ' + f'{horner_ite(n0, x0, list0)}')
    print('Horner rekurencyjnie: ' + f'{horner_rec(n0, x0, list0)}')
