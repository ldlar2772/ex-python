l = []
s = 0
while True:
    x = int(input('digite um numero: '))
    s +=x
    l.append(x)
    y = input('quer continuar? [S/N]\n--> ').upper()
    while y not in ['S','N']:
        y = input('quaer continuar? [S/N]\n--> ').upper()
    if y == 'N':
            break
print(l)
print(len(l))
print(s)