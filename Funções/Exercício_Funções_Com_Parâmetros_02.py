# Criar 5 funções: 1 para um cadastro, 2 para realizar o login, 3 para mudar a senha, 4 para realizar logout e 5 para definir qual opção o usuário deseja escolher. Utilize um loop while para sair do sistema apenas se o usuário desejar (criar a opção 'sair').
# Atente-se as regras:

# - Só é possível realizar um cadastro se não houver nenhum anterior.
# - Só é possível realizar login se houver um cadastro.
# - Só é possível realizar login se o usuário informar corretamente username e senha.
# - Só é possíve alterar a senha se o usuário estiver logado.
# - Só é possível alterar a senha se o usuário informar corretamente a senha atual.
# - Só é possível realizar logout se o usuário estiver logado.

login = False
cadastroFeito = False
op = 0
username = ' '
senha = ' '

def intro():
    global op
    global cadastroFeito
    global login
    while op != 5:
        print('1 - Cadastro\n2 - Login\n3 - Mudar senha\n4 - Logout\n5 - Sair')
        op = int(input('______Opção: '))

        if op == 1:
            if not cadastroFeito:
                cadastro()

            else:
                print('________Cadastro já feito anteriormente_________')

        elif op == 2:
            if cadastroFeito:
                loginSistema()

            else:
                print('_________Faça o cadastro antes de fazer login________')

        elif op == 3:
            if cadastroFeito:
                mudarSenha()

            else:
                print('_________Faça o cadastro antes de alterar a senha_________')

        elif op == 4:
            if login:
                logout()

            else:
                print('________Para dar logout primeiro tem que fazer login né')

        elif op == 5:
            return 0

def cadastro():
    global username
    global senha
    global cadastroFeito
    username = input('_________Digite seu nome de usuário: ')
    senha = input('________Digite sua senha: ')
    cadastroFeito = True
    return intro()

def loginSistema():
    global username
    global senha
    global login
    if not login:
        testeUsuario = input('________Username: ')
        testeSenha = input('_______senha: ')

        if testeUsuario == username and testeSenha == senha:
            login = True

    if login:
        print('_______Você está logado!_________')
    else:
        print('________Username ou senha incorretos_________')

    return intro()

def mudarSenha():
    global login
    global senha
    if login:
        testeSenha = input('_______Senha atual: ')
        if testeSenha == senha:
            senha = input('_______Digite sua nova senha: ')
        else:
            print('_________Senha atual incorreta__________')
    else:
        print('_________Faça login antes________')

    return intro()

def logout():
    global login
    login = False
    print('_________Deslogado!________')
    return intro()

intro()

