def leiaInt(mensagem):
    while True:
        dado = input(mensagem)
        try:
            # Tenta transformar o que foi digitado em um número inteiro
            valor = int(dado)
            return valor  # Se deu certo, retorna o número e sai da função
        except ValueError:
            # Se der erro (letras, símbolos, vazio), cai aqui:
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')

# --- Testando a função no programa principal ---
n = leiaInt('Digite um n: ')
print(f'Você acabou de digitar o número {n}')