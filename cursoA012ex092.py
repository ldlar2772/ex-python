d = {}

ano = int(input('Em qual ano estamos? '))

d['nome'] = input('Digite seu nome: ')
d['adn'] = int(input('Digite seu ano de nascimento: '))
d['idade'] = ano - d['adn']

d['clt'] = int(input('Digite sua carteira de trabalho: '))

if d['clt'] != 0:
    d['adc'] = int(input('Qual ano você foi contratado? '))
    d['salario'] = float(input('Qual seu salário? '))

    contribuicao = ano - d['adc']
    d['aposentadoria'] = d['idade'] + (35 - contribuicao)

print('-=' * 10)

for k, v in d.items():
    print(f'{k}: {v}')