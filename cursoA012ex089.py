lc = []
nm = 0
med = []
while True:
    nome = input(f'qual o nome [{nm}]? ')
    nm+=1
    x = float(input(f'qual a nota 1? '))
    y = float(input(f'qual a nota 2? '))
    m = (x+y)/2
    med.append(m)
    lc.append([nome,[x,y]])
    
    x = input('quer continuar [S/N]?\n--> ').upper()
    while x not in 'SN':
        x = input('quer continuar [S/N]?\n--> ').upper()
    if x == 'N':
        break
print('No.   nome      notas')
for pos, aluno in enumerate(lc):
    print(f'{pos:<4} | {aluno[0]:<10} | {aluno[1][0]:.1f} // {aluno[1][1]:.1f}')
u = int(input(f'deseja acessar a media de qual Numero?\n--> '))
print(f'a media foi de {med[u]:.1f}')
