matriz = []
# eu nao consegui fazer esse!!!

for l in range(3):
    linha = []

    for c in range(3):
        valor = int(input(f'Digite um valor [{l},{c}]: '))
        linha.append(valor)

    matriz.append(linha)

print(matriz)