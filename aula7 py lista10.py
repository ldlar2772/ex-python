a = []
b = []
c = []
for i in range (2):
    x = int(input(f'digite um numero ({i+1}): '))
    y = int(input(f'digite um numero ({i+1}): '))
    a.append(x)
    b.append(y)
for x,y in zip(a,b):
    c.append(x)
    c.append(y)
print(a)
print(b)
print(c)