import moeda
valor = float(input('Digite um valor: R$ '))
print(f'A metade de {valor} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {valor} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando {valor} em 10%, temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Diminuindo {valor} em 13%, temos {moeda.moeda(moeda.diminuir(valor, 13))}')
