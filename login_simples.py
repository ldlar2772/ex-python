usuario_registrado = []
def registrar():
    usuario = {}
    usuario['email'] = input('Digite seu email: ')
    usuario['senha'] = input('digite sua senha: ')
    global usuario_registrado
    #---------------------------------------------------------------------
    if (usuario['email'] == '') or (usuario['senha'] == ''):
        print('Error - email ou senha vazios')
        usuario.clear()
    #---------------------------------------------------------------------
    elif '@' not in usuario['email']:
        usuario.clear()
        print('Error - estrutura do email')
    #---------------------------------------------------------------------
    elif ' ' in usuario['email'] or ' ' in usuario['senha']:
        usuario.clear()
        print('Error - contem espaços')
    #---------------------------------------------------------------------
    else:
        usuario_registrado.append(usuario.copy())
    print()
    print('----------------  ----------------')
    for u in usuario_registrado:
        print(f'email registrado: {u['email']}\nsenha registrada: {u['senha']}')
    print('----------------  ----------------')
    return usuario_registrado
def login():
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    usuario_cadastrado = False
#---------------------------------------------------------------------
    for u in usuario_registrado:
        if u['email'] == email:
            usuario_cadastrado = True 
        
            if u['senha'] == senha:
                print('Login realizado com sucesso!') 
                return 
            else:
                print('Error - senha nao encontrada')
                return 
#---------------------------------------------------------------------
    if not usuario_cadastrado:
        print('Error - usuario não encontrado')
if usuario_registrado == []:
    print('---------------- menu - registrar ----------------')
    print()
    registrar()
print()
while True:
    print()
    print('---------------- registrar - 0 // login - 1 // Sair - 2 ----------------')
    menu = input('Selecione -> ')
    while menu not in ['0','1','2']:
        menu = input('Selecione -> ')
    if menu == '0':
        registrar()
    elif menu == '1':
        login()
    elif menu == '2':
        break
print()
print('----- FIM -----') 