# Faça um programa que calcule a soma dos divisores de um número inteiro definido pelo usuário.
# Ex.: Se o usuário escolher 10, temos 1 + 2 + 5 + 10 = 18.

soma = 0
numero = int(input('Digite o número: '))
for num in range(1, numero+1):
    if numero % num == 0:
       soma = soma + num
print(soma)
