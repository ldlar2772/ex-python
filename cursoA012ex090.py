n = {}
n ['nome'] = input('digite seu nome: ')
n ['média'] = float(input('digite sua media: '))
print(10*'-=')
print(f'o seu nome é: {n['nome']}')
print(f'a sua media é: {n['média']}')
if n['média'] < 7:
    print(f'voce está reprovado!')
else:
    print('voce esta aprovado!')