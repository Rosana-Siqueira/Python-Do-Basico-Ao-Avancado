# Crie um arquivo de texto na pasta onde está seu programa Python. 
# O arquivo deve conter alguns números de 4 dígitos separados por linha, representando números de uma rifa. 
# Após isso, itere no arquivo para colocar valores em uma lista. 
# Por fim, utilize a função choice() para determinar o ganhador.

from random import choice as ch

numerosRifa = []
with open('Rifa.txt') as rifa:
    for num in rifa: 
        numerosRifa.append(int(num)) 

print(f'Número vencedor: {ch(numerosRifa)}. Parabéns!')
