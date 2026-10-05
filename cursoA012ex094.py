d = {}
m = []
pm = []
pmm = []
n = 0
x = 0

while True:
    d['nome'] = input('nome: ')
    n += 1

    d['sexo'] = input('sexo: [M/F] ').upper()
    while d['sexo'] not in 'MF':
        d['sexo'] = input('sexo: [M/F] ').upper()

    if d['sexo'] == 'F':
        m.append(d['nome'])

    d['idade'] = int(input('idade: '))

    x += d['idade']  # soma as idades

    pm.append(d.copy())

    y = input('quer continuar? [S/N] ').upper()
    while y not in 'SN':
        y = input('quer continuar? [S/N] ').upper()

    if y == 'N':
        break

x = x / n  # calcula a média

for pessoa in pm:
    if pessoa['idade'] > x:
        pmm.append(pessoa)

print(f'o total de pessoas cadastradas foram: {n}')
print(f'a media das idade é {x:.1f}')

for z in m:
    print(f'as mulheres cadastradas foram {z}')

print('as pessoas com idades acima da media sao:')
for pessoa in pmm:
    for k, v in pessoa.items():
        print(f'{k} = {v}', end='; ')
    print()

print('<< ENCERRADO >>')