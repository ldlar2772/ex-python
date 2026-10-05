n = []
p = []
i = []
for y in range (20):
    x = int(input('digite um numero: '))
    n.append(x)
    if x%2 == 0:
        p.append(x)
    else:
        i.append(x)
print(f'o total de numeros sao: {n}\n os numeros pares sao: {p}\nos numeros impares sao: {i}')

