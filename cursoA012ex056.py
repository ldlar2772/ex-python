iddm = []
iddf = []
soma = 0
idds = 0
print(10*'-=')
x = int(input('quantas pessoas? '))
for i in range(x):
    print(f'----- {i+1}ª pessoa -----')
    n = str(input('qual seu nome? '))
    idd = int(input('qual sua idade? '))
    s = str(input('qual seu sexo? '))
    soma += idd
    
    if s.lower() == 'masculino' or s.lower() == 'm':
        iddm.append(idd)
        print(iddm)
    if s.lower() == 'feminino' or s.lower() == 'f':
        iddf.append(idd)
        print(iddf)
       
med = soma/x
print(f'a media das idades do grupo é: {med:.1f}')
if iddm:
    print(f'o homem com maior idade do grupo tem: {max(iddm)} anos de idade.')
else:
    print('não há homens no grupo')
for z in iddf:
    if z < 20:
        idds += 1
print(f'{idds} mulheres tem menos de 20 anos.')