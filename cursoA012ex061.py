x = int(input('digite o primeiro termo: '))
x1 = int(input('digite a razao da pa: '))
x2 = int(input('digite o tamanho da pa: '))
x3 = 1
while x3 <= x2:
    print(f'{x} -> ',end = ' ')
    x += x1
    x3 += 1
print('fim')