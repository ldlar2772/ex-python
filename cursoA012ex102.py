def fatorial(num=1,show=False):
    '''
    -> num recebe o valor do fatorial se nao tiver é igual a 1
    -> show quando show = True mostra o passo a passo do calculo
    -> return retorna o vlaor do fatorial f
    '''
    f = 1
    for i in range (num,0,-1):
        f*= i
        if show:
            if i == 1:
                print(f'{i} =',end=' ')
            else:
                print(f'{i} x',end=' ')
    return f
    
    
print(fatorial(8,show=True))
help(fatorial)