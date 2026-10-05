c = 0
s = 0
print('digite [999] para sair')
while True:
    x = int(input('-=-=-=-=-=-=-=-=-=-\ndigite um numero: '))
    s += x
    if x == 999:
        break
    c +=1
    s += x
if c > 0:
    print(f'foram digitado(s) {c} numero(s).')
    print(f'a soma entre os numeros foi de {s}.')
else:
    print('nenhum numero foi digitado.')
