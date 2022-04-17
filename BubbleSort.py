def bubble_sort(numbers: list):
    for i in range(len(numbers)):
        swapped = False
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers


if __name__ == "__main__":
    lista = [12, 3, 0, 4, 7, 2]
    sort_lista = bubble_sort(lista)
    print(*sort_lista)
