# Teste se um arquivo chamado licros.txt não exista pela abertura x, caso o arquivo já exista abra como w+, utilize Try/Except nessa manipulação.
# Imprima na tela qual foi o modo de abertura, escreva no bloco o nome dos três melhores livros que você já leu (um em cada linha) adicionando ao arquivo, feche-o Abra-o novamente e adicione mais um livro ao final do arquivo sem apaga-lo, por fim, leia a versão final.

try:
    with open('livros.txt', 'x') as arq:
        print("Abrimos no modo 'x'")
        arq.write('O Poder do Habito')
        arq.write('\nSteve Jobs')
        arq.write('\nMemórias Póstumas de Brás Cubas')
except FileExistsError:
    with open('livros.txt', 'w+') as arq:
        print("Abrimos o arquivo no modo 'w+'")
        arq.write('O poder do Habito')
        arq.write('\nSteve Jobs')
        arq.write('\nMemórias Póstumas de Brás Cubas')

with open('livros.txt', 'a+') as arq:
    arq.write('\nSherlok Holmes')
    arq.seek(0)
    print(arq.read())

