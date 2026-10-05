'''matriz plus'''

matriz = []

for l in range(3):
    linha = []

    for c in range(3):
        valor = int(input(f'Digite um valor [{l},{c}]: '))
        linha.append(valor)

    matriz.append(linha)

print(matriz)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')