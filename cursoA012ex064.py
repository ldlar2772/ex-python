s = 0
c = 0
n = int(input('digite [999] para sair\n-=-=-=-=-=-=-=-=-=-=-=-\ndigite um numero: '))
while n != 999:
    s += n
    c += 1
    n = int(input('digite um numero: '))
print(f'voce digitou {c} vezes e a soma dos numeros é {s}')