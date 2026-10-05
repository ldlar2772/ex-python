x = int(input('digite o primeiro termo: '))
x1 = int(input('digite a razao da pa: '))
x2 = int(input('digite o tamanho da pa: '))

contador = 1
termo = x

# primeira parte
while contador <= x2:
    print(f'{termo} -> ', end=' ')
    termo += x1
    contador += 1

print('PAUSA')

# segunda parte (mais termos)
y = int(input('Mais quantos termos quer ver? '))

while y != 0:
    contador = 1
    while contador <= y:
        print(f'{termo} -> ', end=' ')
        termo += x1
        contador += 1
    
    print('PAUSA')
    y = int(input('Mais quantos termos quer ver? '))

print('FIM')