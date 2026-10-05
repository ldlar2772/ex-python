import random
x = int(input('qual o tamanho da tupla? '))
n = tuple(random.randint(1,10) for i in range (x))
print(f'os numeros selecionados foram: {n}')
print(f'o maior numero é {max(n)}')
print(f'o menor numero é {min(n)}')