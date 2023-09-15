# 1- Utilize o módulo random e suas funções para realizar os seguintes procedimentos da tabela abaixo:

# ------------------------------------------------------------------------------------------------------------
# |  nº | Função     | Procedimento                                                                           |
# |-----------------------------------------------------------------------------------------------------------|
# |  1  | random()   | Obter um número aleatório inteiro entre 1 e 10 e armazenar em uma variável X           |
# |  2  | randint()  | Obter X números aleatórios inteiros entre 0 e 100 e armazená-los em uma lista          |
# |  3  | shuffle()  | Embaralhar a lista                                                                     |
# |  4  | choice()   | Selecionar um elemento aleatório da lista                                              |
# |  5  | loop       | Imprimir os números da lista que são maiores que o número selecionado                  |
# |-----------------------------------------------------------------------------------------------------------|

from random import (
    random as rd,
    randint as ri,
    shuffle as sh,
    choice as ch
)

listaAle = []
x = round(rd() * 10) 
print(x)
for i in range(x):
    listaAle.append(ri(0, 100))

print(listaAle)

sh(listaAle) 
print(listaAle)

escolhido = ch(listaAle) 
print(f'Número Escolhido: {escolhido}')

print('Números maiores que o escolhido: ', end=' ')
for i in listaAle:
    if i > escolhido:
     print(i, end=' ')
     