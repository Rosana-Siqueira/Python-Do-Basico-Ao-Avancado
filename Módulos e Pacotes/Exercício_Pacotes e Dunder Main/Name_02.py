# Maria e João jogando bingo em família. 
# Cada um possui uma cartela e cada cartela possui 7 números entre 1 e 30, que serão sorteados por uma função, utilizando choice(), contida em um módulo customizado, sendo acessado apenas se o módulo for importado. 
# Os números das cartelas devem ser definidos utilizando comprehesions e choice() no programa principal.
# O primeiro a ter seus 7 números chamados vence. 
# Crie um sistema para representar o jogo, como os números sorteados e a conferência das cartelas. 
# No final apresente o vencedor, os números da cartela do vencedor e os números sorteados.

from random import choice as ch
from Módulo_Exercícios_Bingo import sorteio

numeros = 7 
max = 30 

sorteador = list(range(1, max + 1))
cartelaMaria = [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]

sorteador = list(range(1, max + 1))
cartelaJoao = [sorteador.pop(sorteador.index(ch(sorteador))) for num in range(numeros)]

print(f'Cartela João: {cartelaJoao}')
print(f'Cartela Maria: {cartelaMaria}')
sorteio(cartelaJoao, cartelaMaria, max)
