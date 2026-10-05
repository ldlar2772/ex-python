i = int(input('qual ano voce nasceu? '))
x = 2026 - i
if x <= 9:
    print('MIRIM')
elif x <= 14:
    print('INFANTIL')
elif x <= 19:
    print('JUNIOR')
elif x <=20:
    print('SÊNIOR')
else:
    print('MASTER')