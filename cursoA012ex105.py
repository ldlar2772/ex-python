d = {}
notas = []
s = 0
while True:
    
    n = float(input('Digite sua nota: '))
    notas.append(n)
    s+= n
    
    y = input('Continuar? [S/N]\n-> ').upper()
    while y not in ['S','N']:
        y = input('Continuar? [S/N]\n-> ').upper()
        
    if y == 'N':
        break
x = input('Situação? [S/N]\n-> ').upper()
while x not in ['S','N']:
    x = input('Situação? [S/N]\n-> ').upper()

        
men = notas[0]
d['todas'] = len(notas)
for m in notas:
        
    if m > mai:
        mai = m
    if m < men:
        men = m
d['maior'] = mai
d['menor'] = men
d['media'] = s/d['todas']
if x == 'S':
    if d['media'] >= 7:
        d['situação'] = 'Ótimo'
    elif d['media'] >=5:
        d['situação'] = 'Ok'
    else:
        d['situação'] = 'Ruim'
print(d)