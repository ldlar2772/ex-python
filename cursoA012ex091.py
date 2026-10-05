import random
import time
d = {}
l = []
for i in range (4):
    d[f'jogador ({i+1})']= random.randint(1,6)
l.append(d.copy())
time.sleep(0.5)
print(l)
print('-=' * 15)
print('RANKING DOS JOGADORES')

ordem = sorted(d.items(), key=lambda item: item[1], reverse=True)

for pos, (jogador, valor) in enumerate(ordem, start=1):
    print(f'{pos}º lugar: {jogador} com {valor}')