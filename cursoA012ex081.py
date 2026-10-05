l = []
for z in range(5):
    x = int(input(f'digite um numero {z+1}: '))
    l.append(x)

print(f'foram digitados {len(l)} numeros!')
l.sort()
print(f'em ordem decrescente fica: {l[::-1]}')
if x == 5:
    print('valor 5 foi digitado')
    print(f'o numero 5 esta na posição: {l.index(5)}')
else:
    print('5 nao foi digitado')