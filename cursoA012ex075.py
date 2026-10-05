t = tuple(int(input('digite um numero: '))for i in range (4))
print(f'os numeros digitados foram: {t}')
print(f'o numero 9 apareceu {t.count(9)}')
if 3 not in t:
    print('o tres nao foi digitado!')
else:
    print(f'o tres foi digitado na posição {t.index(3)}')
p = []
for n in t:
    if n%2 == 0:
        p.append(n)
print(f'os numeros pares digitados foram: {p}')