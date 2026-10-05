n = []
m = 0
s = 0
for i in range (4):
    x = float(input('digite um numero: '))
    n.append(x)
    print(n)
    s +=x
m = x/4
print(f'notas: {n}\nmedia: {m}')