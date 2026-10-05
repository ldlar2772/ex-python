c = float(input('valor da casa: '))
s = float(input('qual o salario? '))
t = int(input('quantos anos? '))
vp = c/(t*12)
x = (30/100)*s
if vp < x:
    print('transação aprovada')
else:
    print('transação recusada')