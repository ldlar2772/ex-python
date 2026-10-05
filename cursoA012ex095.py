d = {}
g = []

d['nome'] = input('Digite o nome do jogador: ')
x = int(input(f"quantas partidas {d['nome']} jogou? "))
d['total'] = 0
for i in range (x):
    gols = int(input(f'quantos gols na partida ({i+1})? '))
    g.append(gols)
    d['gols'] = g
    d['total'] += gols
print(d)
print(15*'-=')
for i in range(len(d['gols'])):
    print(f'na partida ({i+1}), fez {d["gols"][i]} gols')
print(f'foi um total de {d["total"]} gols')