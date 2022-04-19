# import random
import math

file0 = open('dane0.txt', 'r')
file1 = open('dane1.txt', 'r')

data0 = []
data1 = []
'''for i in range(100):
    data.append(random.randint(0, 10))
    if i + 1 < 100:
        file0.write(f'{data[i]}' + ' ')
    else:
        file0.write(f'{data[i]}')'''
input_data0 = file0.read().split(' ')
input_data1 = file1.read().split(' ')
for i in range(len(input_data0)):
    data0.append(int(input_data0[i]))
data0.sort()
total = 0
for number in data0:
    total += number
arithmetic_mean0 = total / len(data0)
if len(data0) % 2 == 1:
    median0 = data0[len(data0) // 2]
else:
    median0 = (data0[len(data0) // 2] + data0[len(data0) // 2]) / 2
standard_deviation0 = 0
for number in data0:
    standard_deviation0 += (number - arithmetic_mean0) ** 2
standard_deviation0 = math.sqrt(standard_deviation0 / len(data0))

for i in range(len(input_data1)):
    data1.append(int(input_data1[i]))
data1.sort()
total = 0
for number in data1:
    total += number
arithmetic_mean1 = total / len(data1)
if len(data1) % 2 == 1:
    median1 = data1[len(data1) // 2]
else:
    median1 = (data1[len(data1) // 2] + data1[len(data1) // 2]) / 2
standard_deviation1 = 0
for number in data1:
    standard_deviation1 += (number - arithmetic_mean1) ** 2
standard_deviation1 = math.sqrt(standard_deviation1 / len(data1))

file0.close()
file1.close()
