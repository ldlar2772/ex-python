x = 0
y = int(input('digite um numero: '))
z = int(input('digite um numero: '))
while x != 5:
    x = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair\n-=-=-=-=-=-=-=-=-\n--> '))
    if x == 1:
        print(f'{y} + {z} = {y+z}')
        print('-=-=-=-=-=-=-=-=-')
    elif x == 2:
        print(f'{y} x {z} = {y*z}')
        print('-=-=-=-=-=-=-=-=-')
    elif x == 3:
        if y > z:
            print(f'o maior é {y}')
        else:
            print(f'o maior é {z}')
        print('-=-=-=-=-=-=-=-=-')
    elif x == 4:
        y = int(input('digite um numero: '))
        z = int(input('digite um numero: '))
        print('novos numeros definidos!')
        print('-=-=-=-=-=-=-=-=-')
    elif x == 5:
        print('finalizando...')
    else:
        print('opção inválida')
print('finalizado.')