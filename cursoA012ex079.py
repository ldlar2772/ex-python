l = []
while True:
    x = int(input('digite um numero: '))
    if x not in l:
        l.append(x)
        print('valor adicionado com sucesso!')
    else:
        print('nao vou adicionar haha')
    print(l)
    y = input('Deseja continuar? [S/N]\n--> ').upper()
    while y not in 'SN':
        y = input('Deseja continuar? [S/N]\n--> ').upper()
    
    if y == 'N':
        break
l.sort()
print(l)