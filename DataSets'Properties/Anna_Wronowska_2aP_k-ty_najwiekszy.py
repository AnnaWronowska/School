# przez zliczanie
def counting(array, k):
    count = []
    for i in range(min(array), max(array) + 1):
        count.append(0)
    for i in range(len(array)):
        count[array[i] - min(array)] += 1
    i = len(count) - 1
    while k > 0:
        k -= count[i]
        i -= 1
    return i + 1 + min(array)


# przez wstawianie
def insterting(array, k):
    m = []
    for i in range(k):
        m.append(min(array) - 1)
    m.append(max(array) + 1)
    for i in range(len(array)):
        x = array[i]
        j = - 1
        while x > m[j + 1]:
            j += 1
            m[j] = m[j + 1]
        if j >= 0:
            m[j] = x
    return m[0]


tab = [2, 3, 5, 9, 1, 4, 8, 10, 7, 6]
print(insterting(tab, 3))
