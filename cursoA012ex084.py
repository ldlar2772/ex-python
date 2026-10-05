nome = []
pessoa = []
geral = []
p = 0
while True:
    pessoa.append(input('qual seu nome? '))
    pessoa.append(float(input('quantos kg? ')))
    geral.append(pessoa[:])
    pessoa.clear()
    print(geral)
    p +=1
    x = input('deseja continuar? [S/N]\n--> ').upper()
    while x not in 'SN':
        x = input('deseja continuar? [S/N]\n--> ').upper()
    if x == 'N':
        break

print(f'foram cadastradas {p} pessoas.')
# O key=lambda x: x[1] fala para o Python:
# “compare usando o elemento de índice 1”, ou seja, o peso.
maior = max(geral, key=lambda x: x[1]) 
menor = min(geral, key=lambda x: x[1])

print(f'o maior peso foi de {maior[1]}kg. Peso de {maior[0]}')
print(f'o menor peso foi de {menor[1]}kg. Peso de {menor[0]}')