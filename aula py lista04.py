x = []
while True:
    x1 = float(input('digite sua nota: '))
    x.append(x1)
    y = input('quer continuar? [S/N]\n--> ').upper()
    while y not in ['S','N']:
        y = input('quer continuar? [S/N]\n--> ').upper()
    if y == 'N':
        break
for i in x:
        print(i)