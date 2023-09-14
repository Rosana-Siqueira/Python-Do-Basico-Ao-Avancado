# Foi realizada uma pesquisa de algumas características e gastos de quatro habitantes incluindo:
# nome, sexo, esporte favorito (Natação, Futebol, Volei, Tênis) e idade. Com esses dados faça:

# - Função que armazene os dados em uma lista. Dica: Use dicionários dentro da lista.
# - Calcule a idade média de homens que gostam de natação. Caso não haja homens que gostam de natação chame uma função
# e imprima um aviso de que não há homens que gostam de natação.

def cadastro():
    list = []
    for i in range(4):
        dicionario = dict(nome = input('Digite seu nome: '),
                          sexo = input('Digite M para masculino e F para feminino: '),
                          esporte = input('Escolha seu esporte favorito entre Natação, Futebol, Volei, Tênis: '),
                          idade = int(input('Digite sua idade: ')))
        list.append(dicionario)
    return list

def aviso():
    print('Não tem homens que gostam de natação')
lista = cadastro()
cont = 0
soma = 0

for i in range(4):
    if lista[i]['sexo'] == 'M' and lista[i]['esporte'] == 'Natação':
        soma = soma + lista[i]['idade']
        cont += 1
if cont == 0:
    aviso()
else:
    media = soma / cont
    print(f'A idade média de homens que fazem natação é: {media}')
    

