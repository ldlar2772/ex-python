def voto(x):
    a = 2026 - x
    return a
n = int(input('qual ano voce nasceu? '))
a = voto(n)
print(f'voce tem {a} anos')

if 100 > a >= 18:
    print(f'com {a} anos o voto é obrigatorio!')
elif a >= 100:
    print(f'com {a} anos o voto é opcional!')
else:
    print(f'com {a} anos o voto nao é obrigatorio!')