x = ('zero','um','dois','tres', 'quartro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )

y = int(input('digite um numero de 0 a 20: '))
while y not in range(0,21):
    y = int(input('digite um numero de 0 a 20: '))
    
print(f'voce digitou o numero {x[y]}')