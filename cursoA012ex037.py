while True:
    print('selecione: \n (1) para Binario \n (2) para Octal \n (3) para hexadecimal')
    y = int(input('--> '))
    if y not in [1,2,3]:
        print('====\nerror\n====')
        print('selecione novamente\n----')
        continue
    else:
        x = int(input('escolha um numero para conversão: '))
        
        if y == 1:
            print(bin(x)[2:])
        elif y == 2:
            print(oct(x)[2:])
        elif y == 3:
            print(hex(x)[2:])
        break