import time
def autoc():
    print('contagem 1 até 10 de 1 em 1')
    #-------------------------------------------------------------------
    for i in range(1,10,1):
        print(i,end =' ', flush=True)
        time.sleep(0.25)
    print()
    #-------------------------------------------------------------------
    print(f'{30*'--'}\ncontagem 10 até 0 de 2 em 2')
    for y in range(10,-1,-2):
        print(y,end =' ', flush=True)
        time.sleep(0.25)
    print()
    #-------------------------------------------------------------------
def contador(x,y,z):
    if y > 0:#contagem ate alguma coisa
        y+=1
    elif y == 0:
        y-=1
    elif y < 0:#contagem ate alguma coisa
        y-=1
    #-------------------------------------------------------------------
    if x > y and z > 0: #se o inicio for maior q o fim deixa o passo negativo
        z = z*-1
    #-------------------------------------------------------------------
    if z == 0 and x>y:
        z = -1
    elif z == 0 and y>x:
        z = 1
    #-------------------------------------------------------------------
    print(30*'--')
    #-------------------------------------------------------------------
    if y>0:
        print(f'contagem de {x} até {y-1} de {z} em {z} ')
    elif y<0:
        print(f'contagem de {x} até {y+1} de {z} em {z} ')
    else:
        print(f'contagem de {x} até {y} de {z} em {z} ')
    #-------------------------------------------------------------------
    for t in range(x,y,z):
        print(t,end =' ', flush=True)
        time.sleep(0.25)
    print('FIM!')
    print()
    #-------------------------------------------------------------------
autoc()
#-------------------------------------------------------------------
print(f'{30*'--'}\nagora é sua vez de personalizar a contagem!')
#-------------------------------------------------------------------
contador(x = int(input('inicio: ')),y = int(input('fim: ')),z = int(input('passo: ')))
#-------------------------------------------------------------------