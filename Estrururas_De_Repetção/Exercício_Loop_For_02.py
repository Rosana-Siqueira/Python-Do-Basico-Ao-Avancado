# Faça um programa que imprima os n primeiros múltiplos de 5, sendo n definido pelo usuário.
# Ex.: Se o usuário escolheu n=3, será impresso 5,10,15.

numero = int(input('Digite o número de multiplos de 5 que deseja: '))
for num in range(1,numero+1):
    print(f'{5 * num}')
    