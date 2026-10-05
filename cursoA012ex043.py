x = float(input('qual sua altura? '))
y = float(input('qual o seu peso? '))
imc = y /(x*x)
print(f'{imc:.2f}')
if imc < 18.5:
    print(f'Abaixo do peso, seu imc corresponde a: {imc:.2f}')
elif imc <= 25:
    print(f'voce esta no peso ideal, seu imc corresponde a: {imc:.2f}')
elif  imc <= 30:
    print(f'Sobrepeso, seu imc corresponde a: {imc:.2f}')
elif  imc <= 40:
    print(f'Voce tem Obesidade, e seu imc corresponde a: {imc:.2f}')
else:
    print(f'voce tem obesidade Mórbida, seu imc corresponde a: {imc:.2f}')