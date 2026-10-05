n = int(input('digite um numero: '))

a = 0
b = 1
cont = 0
while cont < n:
    print(a, end=' ')
    prox = a+b
    a = b
    b = prox
    cont += 1