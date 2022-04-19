# naiwnie
def naive(array):
    max_amount = 0
    for i in array:
        tmp_amount = 0
        for j in range(len(array)):
            if array[j] == i:
                tmp_amount += 1
        if tmp_amount > max_amount:
            max_amount = tmp_amount
            max_value = i
    return max_value, max_amount


# naiwnie z modyfikacjami
def modificated(array):
    max_amount = 1
    max_value = array[0] + 1
    for i in range(len(array) - (max_value - 1)):
        tmp_amount = 1
        for j in range(i + 1, len(array)):
            if array[j] == array[i]:
                tmp_amount += 1
        if tmp_amount > max_amount:
            max_amount = tmp_amount
            max_value = array[i]
    return max_value, max_amount


# dla spójnego zbioru danych
def forrange(array):
    index = []
    for i in range(len(array)):
        index.append(0)
    for x in array:
        index[array.index(x)] += 1
    return array[index.index(max(index))], max(index)


# z sortowaniem
def with_sorting(array):
    array.sort()
    max_amount = 0
    tmp_amount = 1
    for i in range(len(array)):
        if i < len(array) - 1 and array[i] == array[i + 1]:
            tmp_amount += 1
        else:
            if tmp_amount > max_amount:
                max_amount = tmp_amount
                max_value = array[i]
            tmp_amount = 1
    return max_value, max_amount


if __name__ == "__main__":
    tab = [1, 2, 3, 4, 5, 2, 1, 10, 6, 7, 8, 9, 1]
    print(with_sorting(tab))
