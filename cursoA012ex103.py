def ficha(j = '',g= ''):
    if j =='' and g=='':
        print(f'o nome do jogador é <desconhecido> e ele fez 0 gols!')
    elif j == '':
        print(f'o nome do jogador é <desconhecido> e ele fez {g} gol(s)!')
    elif g == '':
        print(f'o nome do jogador é {j} e ele fez 0 gols!')
    
    else:
        print(f'o nome do jogador é {j} e ele fez {g} gols!')
j = input('qual o nome do jogador? ')
g = input('quantos gols ele fez? ')
if not g.isnumeric():
    g = 0
ficha(j,g)