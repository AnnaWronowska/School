file = open('vigenere_in.txt', 'r')
file2 = open('vigenere_out.txt', 'w')


data = file.read().split('\n')
key = data[0]
text = data[1]
key2 = ''
var = 0
var2 = 0
alphabets = []
outp = ''

for i in range(26):
    alphabets.append(list(map(chr, range(65 + i, 91))) + list(map(chr, range(65, 65 + i))))

while len(key2) < len(text):
    if text[var] in alphabets[0]:
        key2 += key[var2 % len(key)]
        var += 1
        var2 += 1
    elif text[var] == ' ':
        key2 += ' '
        var += 1

var = 0

while var < len(text):
    if text[var] == ' ':
        outp += " "
        var += 1
    elif text[var] in alphabets[0]:
        x = alphabets[0].index(text[var])
        y = alphabets[0].index(key2[var])
        outp += alphabets[x][y]
        var += 1
key_out = ''
for i in key:
    key_out += alphabets[0][(26 - alphabets[0].index(i)) % 26]

file2.write(key_out + '\n' + outp)
file.close()
file2.close()
