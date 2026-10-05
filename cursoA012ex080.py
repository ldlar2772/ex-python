l = []
for z in range(5):
    x = int(input(f'digite um numero {z+1}: '))
    l.append(x)
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print(l)