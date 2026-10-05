l = []
s = 0
m = 1
for i in range(5):
    x = int(input('digite um numero: '))
    l.append(x)
    s += x
    m *= x
print(f'a soma é: {s}')
print(f'a multiplicao dos valores é: {m}')
print(f'os valores sao: {l}')