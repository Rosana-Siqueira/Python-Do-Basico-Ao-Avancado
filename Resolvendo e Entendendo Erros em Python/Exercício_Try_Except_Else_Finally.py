# Aplique o procedimento Try/Excepet/Else/Finally no seguinte código que realiza um cadastro de formulário para uma pessoa realizar uma viagem:

opcoes_viagem = {1: 'EUA', 2:'Franca', 3:'Japao', 4:'Brasil'}
try:
    nome = input('Digite seu nome: ')
    teste = int(nome)
except ValueError:
    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('Idade deve conter apenas números')
    else:
        try:
            lugar = int(input('Digite o número para escolha do lugar: \n '
            '1 - EUA \n '
            '2 - Franca \n '
            '3 - Japao \n '
            '4 - Brasil \n'))
        except ValueError:
            print('Você deve escolher um número de 1 a 4')
        else:
            try:
                pais = opcoes_viagem[lugar]
            except KeyError:
                print('Você digitou um número fora do intervalo de 1 a 4')
else:
    print('AVISO! Nome deve ser escrito com letras apenas.')
finally:
    print('Cadastro finalizado!')
    