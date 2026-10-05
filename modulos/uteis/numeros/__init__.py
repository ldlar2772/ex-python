def fat(x):
    f = 1
    if x == 1 or x == 0:
        print(f'{x}! = 1')
    else:
        for i in range(x,1,-1):
            f*=i
            print(i,end=' x ')
        print(f'1 = {f}')
