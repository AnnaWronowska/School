file1 = open('in.txt', 'r')
file2 = open('out.txt', 'w')

alphabetL = list(map(chr, range(97, 123)))
alphabetU = list(map(chr, range(65, 91)))
rot13L = list(map(chr, range(110, 123))) + list(map(chr, range(97, 110)))
rot13U = list(map(chr, range(78, 91))) + list(map(chr, range(65, 78)))
inp = file1.read()
outp = ''

for i in inp:
    if i in alphabetL:
        i = rot13L[alphabetL.index(i)]
    elif i in alphabetU:
        i = rot13U[alphabetU.index(i)]
    outp += i
    
file2.write(outp)
file1.close()
file2.close()
