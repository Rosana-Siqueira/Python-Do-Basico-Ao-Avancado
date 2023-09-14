# Criar uma lista e uma tupla com diversos valores, separar os valores máximos e mínimos de cada uma em um conjunto. Por fim, verificar se os 4 valores separados são verdadeiros ou falsos utilizando o any e o all.

lista = [23, 1, 12, 7.65]
tupla = (0, True, 0.54, 0, 54, True)

conjunto = {max(lista), min(lista), max(tupla), min(tupla)}

print(conjunto)

print(any(conjunto))
print(all(conjunto))
