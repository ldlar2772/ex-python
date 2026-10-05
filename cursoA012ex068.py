import random
cont = 0
while True:
    x1 = input(('PAR OU IMPAR: ')).upper()
    x = int(input('digite um numero: '))
    c = random.randint(1,10)
    print(f'computador digitou: {c}')
    print(f'{x} + {c} = {x+c}')
    z = x+c
    if x1 == 'PAR' and z%2 == 0:
        print('Voce ganhou!')
        cont+=1
    elif x1 == 'IMPAR' and z%2 == 1:
        print('Voce ganhou!')
        cont+=1
    else:
        print('perdeu')
        break
print(f'voce ganhou {cont} vezes!')