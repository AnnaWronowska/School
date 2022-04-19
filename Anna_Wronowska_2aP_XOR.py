import random

file = open('xor_in.txt', 'r')
file2 = open('xor_out.txt', 'w')
seed = int(file.readline())
random.seed(seed)
inp = file.read()
outp = ''

file2.write(str(seed) + '\n')

for i in range(len(inp)):
    i = chr(ord(inp[i]) ^ (random.randint(0, 100) % 95 + 32))
    outp += i

file2.write(outp)
file.close()
file2.close()
