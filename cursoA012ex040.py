x = float(input('qual foir sua nota? '))
y = float(input('qual foir sua nota? '))
m = (x+y)/2
if m > 7:
    print('aprovado!!')
elif 5 < m < 7:
    print('recuperação!!')
elif m < 5:
    print('reprovado!!')