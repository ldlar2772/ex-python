while True:
    try:
        numero = int(input('DIgite um numero inteiro: '))
        break
    except ValueError:
        print('voce nao digitou um nuemro inteiro')
while True:
    try:
        numero1 = float(input('DIgite um numero real: '))
        break
    except ValueError:
        print('voce nao digitou um nuemro real')

print(f'voce digitou o numero inteiro: {numero}\nvoce digitou o numero real: {numero1}')