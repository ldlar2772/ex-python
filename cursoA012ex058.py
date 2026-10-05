import random
t = 0
n = random.randint(1,10)
x = int(input('qual numero estou pensando? '))
while x != n:
    t +=1
    print('oops! errou')
    x = int(input('qual numero estou pensando? '))
print(f'voce teve {t} tentativas ate acertar.')