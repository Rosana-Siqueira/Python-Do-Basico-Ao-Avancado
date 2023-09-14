# Criar uma função recursiva (que retorne ela mesma) para armazenar N termos da sequência de Fibonacci em uma lista. N é definição pelo usuário. Ao encontrar os termos, imprimir a lista e finalizar a função.

listaF = []
stop = 0

def fibonacci(stop, a, b, aux):
    global listaF
    listaF.append(a)
    a, b = b, a + b
    aux += 1
    if stop == aux:
        print(listaF)
        return  0
    else:
        return fibonacci(stop, a, b, aux)

while stop < 1:
    stop = int(input('Digite a quantidade de termos: '))

fibonacci(stop, a=1, b=1, aux = 0)

