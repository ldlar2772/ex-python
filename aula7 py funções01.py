while True:
    
    h = int(input('quantas horas? '))
    m = int(input('quantos minutos? '))
    while (24<h or h<0) or (60<m or m<0):
        print('Error')
        h = int(input('quantas horas? '))
        m = int(input('quantos minutos? '))
    if h >12:
        h -=12
        print(f'{h}:{m} PM')
    else:
        print(f'{h}:{m} AM')
    x  = input('deseja continuar? [S/N]\n--> ').upper()
    while x not in 'SN':
        x  = input('deseja continuar? [S/N]\n--> ').upper()
    if x == 'N':
        break