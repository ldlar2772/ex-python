t = ('lapis',1.5,'caneta',2.5,'borracha',0.5)
for pos in range (0,len(t)):
    if pos%2 == 0:
        print(f'{t[pos]:.<30}',end='')
    else:
        print(f'{t[pos]:>7.2f} reais')
        