usuario_cadastro = {}
cadastrados = []

def registrar():
    usuario_cadastro['email'] = input('digite seu email: ')
    usuario_cadastro['senha'] = input('digite sua senha: ')
    if v_email():
        print('Error - email ja cadastrado!')
    else:
        cadastrados.append(usuario_cadastro.copy())
        print('registrado com sucesso!!!')


def login():
    if not cadastrados:
        print('Error - nenhum usuario registrado\nregistrar? S/N')
        sn = input('-> ').upper()
        while sn not in ['S','N']:
            sn = input('-> ').upper()
        if sn == 'S':
            registrar()
        else:
            print('Nenhum usuario registrado')
    else:
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        if {'email': email, 'senha': senha} in cadastrados:
            print('login realizado com sucesso')
        else:
            print('usuario ou senha incorretos')
def v_email():
    for v in cadastrados:
        if usuario_cadastro['email'] == v['email']:
            return True
    return False
def delete():
    if not cadastrados:
        print('Error - nenhum usuario registrado\nregistrar? S/N')
        sn = input('-> ').upper()
        while sn not in ['S','N']:
            sn = input('-> ').upper()
        if sn == 'S':
            registrar()
    else:
        print('selecione um email para deletar\n')

        for d in cadastrados:
            print(d['email'])

        delet = input('-> ')

        for d in cadastrados:
            if delet == d['email']:
                cadastrados.remove(d)
                print('Usuário deletado!')
                return

        print('Email não encontrado!')

    if cadastrados == []:
        print('Error - nao existe nenhum usuario!')
    
        
while True:
    print('0 - registrar // 1 - login // 2 - sair // 3 - excluir usuario')
    op = input('-> ')
    while op not in ['0','1','2','3']:
        op = input('-> ')
    if op == '0':
        registrar()
    elif op == '1':
        login()
    elif op == '3':
        delete()
    else:
        break
print('você saiu\n')
for e in cadastrados:
    print(f'email: {e["email"]}\nsenha: {e["senha"]}\n{len(e["senha"])*"-="}')