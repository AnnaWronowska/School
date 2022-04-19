file1 = open('kompresja_in.txt', 'r')
file2 = open('kompresja_out.txt', 'w')


def compress(s: str):
    count = 1
    outs = ''
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        elif count > 2:
            outs += '!' + f'{count}' + s[i - 1]
            count = 1
        else:
            for j in range(count):
                outs += s[i - 1]
            count = 1
    if count > 1:
        outs += '!' + f'{count}'
    outs += s[len(s) - 1]
    return outs


string = file1.read()
file2.write(compress(string))
