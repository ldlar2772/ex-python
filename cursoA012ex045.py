import random
import time
while True:
    print('selecione:\n----------\n(1) Pedra\n(2) Papel\n(3) Tesoura\n----------')
    y = random.randint(1, 3)
    try:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!!!')
        x = int(input('--> '))
        if x < 1 or x > 3:
            print('error')
            continue
        break
    except ValueError:
        print('Invalid input')
        continue

print(y)
if x == y:
    print('Empate')
elif x == 1 and y == 2:
    print('A maquina sempre vence! HAHAHA')
elif x == 2 and y == 1:
    print('Humano maldito!!')
elif x == 3 and y == 2:
    print('A maquina sempre vence! HAHAHA')
elif x == 2 and y == 3:
    print('Humano maldito!!')
elif x == 3 and y == 1:
    print('A maquina sempre vence! HAHAHA')
elif x == 1 and y == 3:
    print('Humano maldito!!')