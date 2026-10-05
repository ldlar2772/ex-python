ld = []
d = {}
while True:
    lg = []
    
    d['jogador'] = input('qual o nome do jogador? ')
    gol = 0
    p = int(input(f'quantas partidas {d["jogador"]} jogou? '))
    for i in range (p):
        g = int(input(f'quantos gols {d["jogador"]} fez na partida({i+1}): ' ))
        lg.append(g)
        gol += g
    d['gols'] = lg
    d['t-gols'] = gol
    ld.append(d.copy())
    
    x = input('deseja continuar? [S/N]\n--> ').upper()
    while x not in 'SN':
        print('--Error--')
        x = input('deseja continuar? [S/N]\n--> ').upper()
    if x  == 'N':
        break
print()

for z,i in enumerate(ld):
    print(f'{z} - {i}')
while True:
    h = int(input(f'digite um numero de 0 a {len(ld)-1} para especificar\n--> '))
    
    while h < 0 or h >= len(ld):
        print('Error (jogador nao encontrado)')
        h = int(input(f'digite um numero de 0 a {len(ld)-1} para especificar\n--> '))

    print(f'levantamento do jogador {ld[h]["jogador"].upper()}')
    
    for r,b in enumerate(ld[h]["gols"]):
        print(f'no jogo {r+1} fez {b} gols.')
        
    x = input('deseja continuar? [S/N]\n--> ').upper()
    while x not in 'SN':
        print('--Error--')
        x = input('deseja continuar? [S/N]\n--> ').upper()
    if x  == 'N':
        break