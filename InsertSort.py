def insert_sort_lin(d):
    for i in range(len(d) - 2, 0, -1):
        x = d[i]
        j = i + 1
        while j < len(d) and x > d[j]:
            d[j - 1] = d[j]
            j += 1
        d[j - 1] = x
    print(*d)


def insert_sort_bin(d):
    for i in range(len(d) - 2, 0, -1):
        x = d[i]
        jp = i
        jk = len(d)
        while jk - jp > 0:
            j = (jp + jk) // 2
            if x <= d[j]:
                jk = j
            else:
                jp = j
        for j in range(i, jp, -1):
            d[j] = d[j + 1]
        d[jp] = x
    print(*d)


lista = [0, 9, 3, 2, 6, 7, 13, 12, 74, 1]
print(*lista)
insert_sort_lin(lista)
sorted(lista)
insert_sort_bin(lista)
