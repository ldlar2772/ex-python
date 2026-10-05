import time
def tit(txt):
    x = print(len(txt)*'-',txt,len(txt)*'-')
while True:
    ajuda = input('Digite um comando: ')
    time.sleep(0.5)
    tit('Acessando manual')
    time.sleep(1)

    help(ajuda)
    time.sleep(0.5)
    tit('Deseja continuar? [S/N]')
    y = input('-> ').upper()
    while y not in ['S','N']:
        y = input('-> ').upper()
    if y == 'N':
        break
tit('FIM!')