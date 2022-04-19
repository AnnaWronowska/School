def find_leader(array):
    var = 0
    leader = 0
    # tab = [1, 2, 3, 4, 1, 1, 1, 1, 6, 7, 1, 9, 1]
    for i in range(len(array)):
        if var > 0:
            if leader == array[i]:
                var += 1
            else:
                var -= 1
        else:
            leader = array[i]
            var = 1
    if var == 0:
        print('Brak lidera w zbiorze')
        return
    else:
        var = 0
        for i in range(len(array)):
            if array[i] == leader:
                var += 1
        if var >= len(array) // 2:
            print('Liderem jest ' + f'{leader}' + ' wystepuje ' + f'{var}' + ' razy')
            return
        else:
            print('Brak lidera w zbiorze')
            return


if __name__ == "__main__":
    tab = [1, 2, 3, 4, 1, 1, 1, 1, 6, 7, 1, 9, 1]
    find_leader(tab)
