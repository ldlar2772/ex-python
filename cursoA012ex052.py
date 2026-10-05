x = int(input('digite um numero: '))
s = 0
for i in range(1,x,+1):
    if x%i == 0:
        s +=1
print(s)
if s < 2:
    print('primo')
else:
    print('normal')