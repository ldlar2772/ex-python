while True:
    x = int(input('digite um numero para a tabuada: '))
    if x < 0:
        break
    print('--'*15)
    for i in range (1,11):
        print(f'{x} x {i} = {x*i}')
    print('--'*15)
