x = []
while True:
    y = input('digite um nome: ')
    x.append(y)
    print(x)
    x1 = int(input('deseja substituir qual posição? [-1 para nao]\n--> '))
    while x1 < -1 or x1 >= len(x):
        x1 = int(input('deseja substituir qual posição? [-1 para nao]\n--> '))
    if x1 != -1:
        y1 = input(f'digite o novo nome da posição {x1}\n--> ')
        x[x1] = y1
        print(x)
    else: 
        print('nenhum nome alterado')
    y1 = input('quer continuar? [S/N]\n--> ').upper()
    while y1 not in ['S','N']:
        y1 = input('quer continuar? [S/N]\n--> ').upper()
    
    if y1 == 'N':
        break
print(x)
print(len(x))
    