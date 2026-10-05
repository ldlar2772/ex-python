i = []
a = []
for z in range (1):
    x = int(input(f'qual sua idade ({z+1})? '))
    i.append(x)
    y = float(input(f'qual sua altura({z+1})? '))
    a.append(y)
print(f'as idades digitadas sao: {i[::-1]}')
print(f'as alturas digitadas sao: {a[::-1]}')