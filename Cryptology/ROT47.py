file1 = open("in.txt", "r")
file2 = open("out.txt", "w")

alphabet = list(map(chr, range(33, 127)))
rot47 = list(map(chr, range(80, 127))) + list(map(chr, range(33, 80)))
inp = file1.read()
outp = ""

for i in inp:
    if i in alphabet:
        i = rot47[alphabet.index(i)]
    outp += i

file2.write(outp)
file1.close()
file2.close()
