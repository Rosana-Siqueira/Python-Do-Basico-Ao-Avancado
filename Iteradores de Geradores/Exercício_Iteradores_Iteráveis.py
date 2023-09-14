# Um estudante do Curso Programando Ideias acabou de assistir a aula de diferença entre iteráveis e iteradores, para praticar mais, criou um programa que realiza o processo de um for,  porém sem utilizar a ferramenta for diretamente, segue o código desenvolvido: o estudante percebeu que o código estava apresentando o seguinte erro:
# TypeError: 'List' object is not on iterator
# Porém, não sasbe como corrigir. Altere o programa do estudante para fazer funcionar corretamente e explique o que aconteceu.

def desmembra_iteravel(iteravel):
    iterador = iter(iteravel)
    while True:
        try:
            print(next(iterador))
        except StopIteration:
            print('Chegamos ao último elemento')
            break

desmembra_iteravel([1, 2, 3, 4, 5, 6, 7, 8])
