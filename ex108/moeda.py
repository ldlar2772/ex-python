def metade(valor):
    return valor/2
def dobro(valor):
    return valor*2
def aumentar(valor,taxa):
    tx = taxa/100
    return (valor*tx) + valor
def diminuir(valor,taxa):
    tx = taxa/100
    return  valor-(valor*tx)
def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')
