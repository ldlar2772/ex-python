a = int(input('que ano voce nasceu?'))
ex = 2026 - a
if ex < 18:
    print('ainda vai se alistar')
elif ex == 18:
    print('hora de se alistar')
else:
    print('passou do tempo')