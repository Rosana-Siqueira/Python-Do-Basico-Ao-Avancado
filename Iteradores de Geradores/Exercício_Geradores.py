# Crie uma lista que armazene inteiros de um usuário em um loop até que o usuário não deseje mais adicionar, trate o erro com try/except caso o usuário digite uma letra ao invés de um número.
# Passe essa lista para uma função geradora que reconhecerá quais são os números primos dentro da lista passada inicialmente.
# Caso seja um número primo, retorne pelo método yield, caso contrário passe para o próximo número.
# Ao final, imprima os valores retornados pelo yield em forma de tupla.

def primos_list(lista):
    for item in lista:
        divisor = 1
        numero_divisores = 0
        while divisor <= item:
            if item % divisor == 0:
                numero_divisores += 1
                divisor += 1
            else:
                divisor += 1
        if numero_divisores == 2:
            yield item

lista = []
sair = ''
while sair != 'sim':
    try:
        lista.append(int(input('Número: ')))
    except ValueError:
        print('Deve ser um número')
    sair = input('Deseja parar? ')

tuple_primos = tuple(primos_list(lista))
print(f'Tupla contendo todos primos: {tuple_primos}')
