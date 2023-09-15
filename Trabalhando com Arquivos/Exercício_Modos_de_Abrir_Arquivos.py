# Faça um programa utilizando um arquivo chamado 'NotasEscola.txt' para gerenciar as notas de alunos de uma classe. 
# O main deve conter um menu com as seguintes opções: a) inserir alunos e notas, b) Exibir os alunos e média final, c) Alunos aprovados e reprovados, d) Sair. 
# Produza uma função para cada opção.

def inserir():
    with open('NotasEscola.txt', 'a') as NE: 
        NE.write('Aluno(a): ' + input('Aluno(a): ') + ' ' + 'Nota: ' + input('Nota: '))
        NE.write('\n')
    print('\nDados Inseridos!\n')

def exibir():
    with open('NotasEscola.txt') as NE:
        print(NE.read())
    print('\nDados apresentados!\n')

def situacao():
    with open('NotasEscola.txt') as NE:
        listaLinhas = NE.readlines()
        for dado in listaLinhas:
            id1 = dado.index(':') 
            id2 = dado.index('Nota') 
            nome = dado[id1 + 1:id2 - 1] 
            id3 = dado.index(':', 10) 
            nota = float(dado[id3 + 1:])
            if nota >= 6:
                print(f'{nome} APROVADO!')
            else:
                print(f'{nome} REPROVADO!')
        print('\n')

op = 1

while op != 0:
    print('Menu:\n1 - Inserir aluno(a) e nota\n2 - Exibir alunos e notas\n3 - Anulos aprovados e '
'reprovados\n4 - Sair')
    op = int(input('Opção: '))

    if op == 1:
        inserir()
    elif op == 2:
        exibir()
    elif op == 3:
        situacao()
    else:
        break