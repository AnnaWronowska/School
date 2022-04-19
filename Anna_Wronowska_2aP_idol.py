def find_idol_naive(array):
    idols = [True for i in range(len(array))]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] and i != j:
                idols[i] = False
            elif i != j:
                idols[j] = False
    for i in idols:
        if i:
            print('Idolem jest ' + f'{idols.index(i) + 1}')
            return
    print('Brak idola w zbiorze')
    return


def find_idol(idols):
    candidate = 0
    for i in range(len(idols)):
        if idols[candidate][i]:
            candidate = i
    i = 0
    for i in range(len(idols)):
        if i != candidate and idols[i][candidate] is False and idols[candidate][i] is True:
            print('Brak idola w zbiorze')
            return
    print('Idolem jest ' + f'{candidate + 1}')
    return


tab = [[True, False, True, False, True, False, False, True, False, False],
       [False, True, False, False, False, False, False, True, False, True],
       [False, True, True, False, False, False, False, True, True, False],
       [False, False, False, True, False, False, False, True, False, False],
       [True, False, False, False, True, False, False, True, False, False],
       [False, True, False, True, False, True, False, True, False, True],
       [False, False, True, False, True, False, True, True, False, False],
       [False, False, False, False, False, False, False, True, False, False],
       [False, True, False, False, False, False, False, True, True, False],
       [True, False, False, False, False, False, False, True, False, True]]

find_idol(tab)
