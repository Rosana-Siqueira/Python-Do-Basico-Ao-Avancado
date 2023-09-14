# Para cada número par em um range de 1 a 9, adicione esse número elevado ao quadrado no conjunto, se o número for impar adicione 2 elementos, 1 por vez: 'Sou', 'Impar'. Qual foi a resposta?
# Por que 'Sou', 'Impar' só apareceu uma vez?

conjunto = set({})
for numero in range(1,10):
    if numero % 2 == 0:
        conjunto.add(numero ** 2)
    else:
        for num in range(0,2):
            if num == 0:
                conjunto.add('Sou')
            else:
                conjunto.add('Impar')
print(conjunto)
Resultado: {64, 4, 36, 'Sou', 'Impar', 16}
