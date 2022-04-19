# my first ever python code
def check(x):
    reszta=f'{x}='
    j=len(reszta)-1
    while x!=0:
        i=0
        while denominations[i]>x:
            i=i+1
        if reszta[j]=='=':
            reszta=reszta+f'{denominations[i]}'
        else:
            reszta=reszta+'+'+f'{denominations[i]}'
        j=j+1
        x=x-denominations[i]
    print(reszta)
denominations=[500, 200, 100, 50, 20, 10, 5, 2, 1]
change=int(input("Podaj reszte "))
check(change)
