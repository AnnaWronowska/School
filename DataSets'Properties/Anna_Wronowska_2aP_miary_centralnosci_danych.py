import math


def find_arithmetic_mean(numbers: list):
    return sum(numbers) / len(numbers)


def find_median(numbers: list):
    if len(numbers) % 2 == 0:
        return data0[len(data0) // 2]
    else:
        return (data0[len(data0) // 2] + data0[len(data0) // 2]) / 2


def find_standard_deviation(numbers: list):
    standard_deviation = 0
    arithmetic_mean = find_arithmetic_mean(numbers)
    for number in numbers:
        standard_deviation += (number - arithmetic_mean) ** 2
    standard_deviation = math.sqrt(standard_deviation / len(numbers))
    return standard_deviation


file0 = open('dane0.txt', 'r')
file1 = open('dane1.txt', 'r')

data0 = list(map(int, file0.read().split(' ')))
data1 = list(map(int, file1.read().split(' ')))

print(find_arithmetic_mean(data0))
print(find_median(data0))
print(find_standard_deviation(data0))

print(find_arithmetic_mean(data1))
print(find_median(data1))
print(find_standard_deviation(data1))

file0.close()
file1.close()
