def matriz_ordem():
  linha = int(input('qual a linha? '))
  coluna = int(input('qual a coluna? '))
  return linha, coluna

linha, coluna = matriz_ordem()

def m3x3(m):
  det = ((m[0][0] * m[1][1] * m[2][2]) + (m[0][1] * m[1][2] * m[2][0]) + (m[0][2] * m[1][0] * m[2][1])) - ((m[2][0] * m[1][1] * m[0][2]) + (m[2][1] * m[1][2] * m[0][0]) + (m[2][2] * m[1][0] * m[0][1]))
  return det

def sub_matriz(m, i, j):
  return [linha[:j] + linha[j+1:] for linha in (m[:i] + m[i+1:])]

def laplace(m):
  n = len(m)

  if n == 3:
    return m3x3(m)

  det = 0

  for j in range(n):
    cofator = ((-1) ** j) * m[0][j] * laplace(sub_matriz(m, 0, j))
    det += cofator

  return det

confirma = input(f'a matriz digitada é de ordem ({linha} x {coluna}) S/N?\n--> ').upper()

while confirma not in ['S', 'N']:
  confirma = input(f'a matriz digitada é de ordem ({linha} x {coluna}) S/N?\n--> ').upper()

if confirma == 'N':
  linha, coluna = matriz_ordem()

matriz = []

for l in range(linha):
    linha_atual = []

    for c in range(coluna):
        num = int(input(f'qual o numero da posição A{l+1},{c+1}? '))
        linha_atual.append(num)

    matriz.append(linha_atual)

print("matriz final:")

for linha_matriz in matriz:
    for numero in linha_matriz:
        print(f"[{numero}]", end=" ")

    print()

print('-------DETERMINANTE-------')

if linha == 2 and coluna == 2:
  det = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])

  print(f'o determinante da matriz de ordem (2x2) é: {det}')


elif linha == 3 and coluna == 3:
  det = m3x3(matriz)

  print(f'o determinante da matriz de ordem (3x3) é: {det}')


elif linha == coluna and linha >= 4:
  det = laplace(matriz)

  print(f'o determinante por Laplace para a matriz de ordem ({linha}x{coluna}) é: {det}')


else:
  print('impossivel calcular pois nao é uma matriz quadrada!!!')