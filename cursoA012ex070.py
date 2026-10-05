c = 0
s = 0
c1 = 0
while True:
    x1 = input('qual o nome do produto? ')
    x = float(input('qual o valor do produto? '))
    c +=1
    y = input('deseja continuar [S/N]\n--> ').upper()
    while y not in ['S','N']:
        y = input('deseja continuar [S/N]\n--> ').upper()
    s +=x
    if x > 1000:
        c1+=1
    if y == 'N':
        print(f'o valor dos produtos é: {s}')
        print(f'sao {c1} produtos que custam mais de 1000')
        break