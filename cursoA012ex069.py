ci = 0
cm = 0
cf = 0
while True:
    i = int(input('qual sua idade? '))
    
    s = input('qual seu sexo [F/M]? ').upper()
    while s not in ['F','M']:
        s = input('qual seu sexo [F/M]? ').upper()

    x = input('deseja continuar [S/N]\n--> ').upper()
    while x not in ['S','N']:
        x = input('deseja continuar [S/N]\n--> ').upper()

    if i > 18:
        ci +=1
    if s == 'M':
        cm +=1
    if s == 'F' and i < 20:
        cf +=1
    if x == 'N':
        break
print(f'{ci} pessoas tem mais de 18 anos')
print(f'{cm} pessoas sao do sexo Masculino')
print(f'{cf} mulheres tem menos de 20 anos')