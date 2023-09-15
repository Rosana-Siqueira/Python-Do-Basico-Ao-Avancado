# Criar um módulo customizado com duas funções (Cálculo de quantidade de números pares e impares em uma lista qualquer). 
# Em seguida, execute as funções passando como argumento uma lista de números naturais.

from Módulo_Exercícios_Customizados import contaPares as cp, contaImpares as ci

numeros = [3, 5, 4, 7, 32, 21, 765, 86, 32, 575, 12, 43, 876, 87, 43, 21, 3, 12, 453]

print(cp(numeros))
print(ci(numeros))
