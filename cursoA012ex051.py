x = int(input('digite o primeiro numero: '))
y = int(input('qual a razão? '))
for i in range(1,11):
    i = (x-y)+i*y
    print(i, end=' ')