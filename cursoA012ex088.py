import random
import time

x = int(input('quantos jogos deseja fazer? '))

for i in range(x):
    jogo = []

    while len(jogo) < 6:
        n = random.randint(1, 60)

        if n not in jogo:
            jogo.append(n)

    jogo.sort()

    print(f'Jogo {i+1}: {jogo}')

    time.sleep(0.01)
import time

x = int(input('quantos jogos deseja fazer? '))

for i in range(x):
    jogo = []

    while len(jogo) < 6:
        n = random.randint(1, 60)

        if n not in jogo:
            jogo.append(n)

    jogo.sort()

    print(f'Jogo {i+1}: {jogo}')

    time.sleep(0.5)