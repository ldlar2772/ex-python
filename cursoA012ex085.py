l = [[],[]]

for i in range (7):
    x = int(input(f'digite um numero [{i+1}]: '))
    
    if x %2==0:
        l[0].append(x)
        l[0].sort()
    else:
        l[1].append(x)
        l[1].sort()
print(l[0])
print(l[1])