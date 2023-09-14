# Criar duas listas de mesmo tamanho preenchidas com números inteiros e retornar outra lista com a soma das duas listas sendo uma delas invertida (indice 0 com indice 9 para uma lista de tamanho 10, por exemplo), utilizando lambda e comprehensions para iterar em ambas.

lista1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lista2 = [160, 11, 50, 22, 43, 24, -12, 24, 542, 217]
lista3 = []

lista2.reverse()
soma = lambda lista1, lista2: [lista1[ind] + lista2[ind] for ind in range(0, 10)]
result = soma(lista1, lista2)
lista3.append(result)
print(lista3)
