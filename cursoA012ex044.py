v = float(input('Qual o valor do produto? '))

print('----------\nSelecione uma forma de pagamento:\n----------\n(dch) Dinheiro ou Cheque.\n(c) Cartão\n(2xc) 2x no Cartão.\n(3xc) 3x ou mais Cartão.\n----------')

d = input('--> ')

if d == 'dch':
    v = v - (v * 0.10)
    print(f'À vista (dinheiro/cheque): R$ {v:.2f}')

elif d == 'c':
    v = v - (v * 0.05)
    print(f'À vista no cartão: R$ {v:.2f}')

elif d == '2xc':
    print(f'2x no cartão (preço normal): R$ {v:.2f}')

elif d == '3xc':
    v = v - (v * 0.20)
    print(f'3x ou mais no cartão: R$ {v:.2f}')

else:
    print('Opção inválida!')