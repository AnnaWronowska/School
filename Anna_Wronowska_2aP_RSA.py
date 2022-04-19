import random
from math import sqrt


file = open('rsa_in.txt', 'r')
file1 = open('rsa_out.txt', 'w')


def eratostenes(x):
    tmpprimes = []
    for i in range(2, x + 1):
        tmpprimes.append(i)
    for i in range(2, int(sqrt(len(tmpprimes))) + 1):
        for j in range(2 * i, x + 1, i):
            if j in tmpprimes:
                tmpprimes.remove(j)
    return tmpprimes


def nwd(a, b):
    if a == 0:
        return b
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def modulo_power(x, w):
    a = 1
    while w > 0:
        if w % 2:
            a = (a * x)
        x = x ** 2
        w = w // 2
    return a


def encryption(message, e, n):
    chars = list(map(ord, list(message)))
    tmpencrypted = []
    for i in range(len(chars)):
        tmpencrypted.append(modulo_power(chars[i], e) % n)
    return tmpencrypted


def decryption(ciphered_list, d, n):
    tmpdecrypted = ''
    for i in range(len(ciphered_list)):
        tmpdecrypted += chr(modulo_power(ciphered_list[i], d) % n)
    return tmpdecrypted


choice = int(input("Wybierz opcje:\n1: generacja klucza\n2: szyfrowanie\n3: deszyfrowanie\n"))
if choice == 1:
    m = 120
    primes = eratostenes(m)
    p = random.choice(primes)
    primes.remove(p)
    q = random.choice(primes)
    euler = (p - 1) * (q - 1)
    n = p * q
    e = 3
    while nwd(e, euler) != 1:
        e += 2
    d = 2
    while e * d % euler != 1:
        d += 1
    print(f'Klucz publiczny: {n}, {e}\nKlucz prywatny: {n}, {d}')

elif choice == 2:
    plaintext = file.read()
    e = int(input('Podaj e\n'))
    n = int(input('Podaj n\n'))
    encrypted = encryption(plaintext, e, n)
    for i in encrypted:
        file1.write(f'{i}' + '\n')

elif choice == 3:
    ciphered_message = list(map(int, file.read().split('\n')))
    d = int(input('Podaj d\n'))
    n = int(input('Podaj n\n'))
    decrypted = decryption(ciphered_message, d, n)
    file1.write(decrypted)

file.close()
file1.close()
