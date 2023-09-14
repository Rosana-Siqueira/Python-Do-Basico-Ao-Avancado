# Crie um sistema de cadastro e login de um site, utilizando um username e senha informados pelo usuário.

login = False
print('Bem-vindo(a) ao cadastro do site!')
username = input('Crie seu nome de usuário: ')
senha = input('Crie sua senha: ')

print('\n_______LOGIN_________')
if input('Usuário: ') == username and input('Senha: ') == senha:
    login = True

if login:
    print(f'\nBem-vindo(a) {username}')
else:
    print('Tente novamente!')
    