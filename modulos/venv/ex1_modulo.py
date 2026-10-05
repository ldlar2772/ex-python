from uteis import numeros
while True:
    for i in range(2):
        x = int(input('Digite um número: '))
        numeros.fat(x)
    y = input('Deseja continuar? [S/N]\n-> ').upper()
    while y not in ['S','N']:
        y = input('Deseja continuar? [S/N]\n-> ').upper()
    if y == 'N':
        break
