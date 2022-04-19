def create_matrix(key):
    tmpmatrix = []
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for i in range(len(key)):
        if key[i] == 'j':
            key[i] = 'i'
    for i in key:
        if i not in tmpmatrix:
            tmpmatrix.append(i)
    for i in alphabet:
        if i not in tmpmatrix:
            tmpmatrix.append(i)
    matrix = []
    for i in range(5):
        matrix.append('')
    matrix[0] = tmpmatrix[0:5]
    matrix[1] = tmpmatrix[5:10]
    matrix[2] = tmpmatrix[10:15]
    matrix[3] = tmpmatrix[15:20]
    matrix[4] = tmpmatrix[20:25]
    return matrix


def message_to_digraphs(original_message):
    message = list(original_message)
    for i in range(len(message)):
        if ' ' in message:
            message.remove(' ')
    i = 0
    while i < len(message):
        if message[i] == message[i + 1]:
            message.insert(i + 1, 'X')
        i += 2
    if len(message) % 2 == 1:
        message.append('X')
    i = 0
    grouped = []
    while i < len(message):
        grouped.append(message[i:i + 2])
        i += 2
    return grouped


def find_position(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x = i
                y = j
    return x, y


def encrypt(message, key):
    message = message_to_digraphs(message)
    key_matrix = create_matrix(key)
    encrypted = []
    for i in message:
        x1, y1 = find_position(key_matrix, i[0])
        x2, y2 = find_position(key_matrix, i[1])
        if x1 == x2:
            encrypted.append(key_matrix[x1][(y1 + 1) % 5])
            encrypted.append(key_matrix[x1][(y2 + 1) % 5])
        elif y1 == y2:
            encrypted.append(key_matrix[(x1 + 1) % 5][y1])
            encrypted.append(key_matrix[(x2 + 1) % 5][y1])
        else:
            encrypted.append(key_matrix[x1][y2])
            encrypted.append(key_matrix[x2][y1])
    return encrypted


def cipher_to_digraphs(cipher):
    i = 0
    grouped = []
    while i < len(cipher):
        grouped.append(cipher[i:i + 2])
        i += 2
    return grouped


def decrypt(cipher, key):
    cipher = cipher_to_digraphs(cipher)
    key_matrix = create_matrix(key)
    plaintext = []
    for i in cipher:
        x1, y1 = find_position(key_matrix, i[0])
        x2, y2 = find_position(key_matrix, i[1])
        if x1 == x2:
            if y1 == 4:
                y1 = -1
            if y2 == 4:
                y2 = -1
            plaintext.append(key_matrix[x1][y1 - 1])
            plaintext.append(key_matrix[x1][y2 - 1])
        elif y1 == y2:
            if x1 == 4:
                x1 = -1
            if x2 == 4:
                x2 = -1
            plaintext.append(key_matrix[x1 - 1][y1])
            plaintext.append(key_matrix[x2 - 1][y2])
        else:
            plaintext.append(key_matrix[x1][y2])
            plaintext.append(key_matrix[x2][y1])

    for i in range(len(plaintext)):
        if plaintext[i] == 'X':
            plaintext.remove('X')

    output = ''
    for i in plaintext:
        output += i
    return output.lower()


order = int(input('Wybierz :\n1 - Szyfrowanie \n2 - Deszyfrowanie\n'))
if order == 1:
    key = input('Podaj klucz\n')
    message = input('Podaj wiadomosc\n')
    print(create_matrix(key.upper()))
    print(encrypt(message.upper(), key.upper()))
elif order == 2:
    key = input('Podaj klucz\n')
    ciphered = input('Podaj zaszyfrowana wiadomosc\n')
    print(decrypt(ciphered.upper(), key.upper()))
else:
    print('Error')
