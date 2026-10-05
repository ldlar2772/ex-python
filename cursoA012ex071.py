x = int(input('qual o valor a ser sacado? '))
ced50 = x//50
x = x %50

ced20 = x//20
x = x%20

ced10 = x//10
x = x%10

ced1 = x//1

print(f'Cédulas de 50: {ced50}')
print(f'Cédulas de 20: {ced20}')
print(f'Cédulas de 10: {ced10}')
print(f'Cédulas de 1: {ced1}')