l = []
i = []
p = []
while True:
    x = int(input('digite um numero: '))
    l.append(x)
    y = input('continuar? [S/N]\n--> ').upper()
    while y not in 'SN':
        y = input('continuar? [S/N]\n--> ').upper()
    
    if x%2==0:
        p.append(x)
    else:
        i.append(x)
    if y == 'N':
        break
print(f'os numeros pares sao: {p}')
print(f'os numeros impares sao: {i}')
print(f'os numeros digitados foram: {l}')
