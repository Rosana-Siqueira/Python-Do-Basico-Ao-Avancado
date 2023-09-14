# 1 - Calcule o fatorial de n utilizando loop for, e depois utilizando reduce. O resultado é o mesmo?


n = int(input('Fatorial de: '))
fat = 1

for i in range(1, n+1):
    fat *= i

print(f'Fatorial loop for: {fat}')

from functools import reduce

lista = [1]
lista.extend(range(1, n+1))

fat = reduce(lambda x, y: x * y, lista)
print(f'Fatorial reduce: {fat}')
