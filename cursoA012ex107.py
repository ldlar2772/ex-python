import modulos.uteis.numeros.ex107 as ex107
valor = float(input('Digite um valor: R$ '))
print(f'A metade de {valor} é {ex107.metade(valor)}')
print(f'O dobro de {valor} é {ex107.dobro(valor)}')
print(f'Aumentando {valor} em 10%, temos {ex107.aumentar(valor, 10)}')
print(f'Diminuindo {valor} em 10%, temos {ex107.diminuir(valor, 10)}')