# Média dos 5 primeiros números primos da sequencia Fibonacci

# - O que é a Sequencia Fibonacci?
# 1,1,2,3,5,8,13,21,34,55...

# Agora aplicando a condição de ser numero primo:

# - condição:
# a) Numeros primos deve ser maiores do que 1.
# b) Numeros primos são apenas divisiveis por ele mesmo e o numero 1.

anterior = 0
proximo = 1
parada = 1
soma = 0
while parada <= 5:
    proximo = proximo + anterior
    anterior = proximo - anterior
    divisor = 1
    num_divisores_inteiros = 0
    while divisor <= proximo:
        if proximo % divisor == 0:
            num_divisores_inteiros += 1
        divisor += 1
    if num_divisores_inteiros == 2:
        soma = soma + proximo
        print(proximo)
        parada += 1

print(soma/5)
