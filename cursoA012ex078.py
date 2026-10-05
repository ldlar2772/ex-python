l = []
for i in range (5):
    x = int(input())
    l.append(x)
    print(l)
print(f'o maior valor é: {max(l)} e esta na posição {l.index(max(l))}')
print(f'o menor valor é: {min(l)} e esta na posição {l.index(min(l))}')
