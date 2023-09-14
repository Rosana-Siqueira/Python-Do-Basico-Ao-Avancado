# Faça uma função que receba um número inteiro maior que zero e retorne a soma de todos os algarismos. 
# Caso o valor seja negativo retorne ‘Número inválido’.
# Exemplo: 251 = 2 + 5 + 1 = 8

def soma_algarismo(numero): 
    divisor = 1
    num_algarismo = 0
    while True: 
        if (numero // divisor) == 0: 
            break
        else:
            num_algarismo = num_algarismo + 1
            divisor += 10
    soma = 0
    for valor in range(num_algarismo):
        soma = soma + ((numero //(10 ** valor)) % 10)
    return soma


numero = int(input('Digite um numero: '))
if numero >= 0:
    print(soma_algarismo(numero))
else:
    print('Numero Inválido')
    