s = 0 
y = input('deseja iniciar? [S/N]\n--> ').upper()
c = 0
z = []
while y != 'N' :
    n = float(input('digite um nuemro: '))
    s +=n
    z.append(n)
    c +=1
    y = input('quer continuar? [S/N]\n--> ').upper()
if c > 0:
    m = s/c
    print(f'a média é {m}')
    print(f'o maior valor é {max(z)}')
    print(f'o menor valor é {min(z)}')
else:
    print('nenhum numero foi digitado.')