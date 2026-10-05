import time
def maior(*num):
    print('Analisando os valores passados...')
    for i in num:
        print(i,end=' ',flush=True)
        time.sleep(0.25)
    print(f'\nForam informados {len(num)} ao todo.')
    if len(num) == 0:
        print('o maior valor informado foi 0')
    else:
        time.sleep(0.5)
        print(f'o maior valor foi {max(num)}.')
        time.sleep(0.5)
        print(30*'--')
maior(6)