# Descubra quais erros estao presentes nos códigos abaixo:

# a-
nome = 'Mark'
# print(int(nome)) # Nao é possível transformar letras em inteiros
# Correto:
nome = 'Mark'
print(nome)
# b- 
frase = 'Eu sou seu pai'
print(frase[-1::]) # O certo é utilizar [::-1]
frase = 'Eu sou seu pai'
print(frase[::-1])
# c- 
filme = 'Avatar'
# print('A maior bilheteria de 2009 foi {filme}') # Falta acrescentar a letra f antes do primeiro '
filme = 'Avatar'
print(f'A maior bilheteria de 2009 foi {filme}')
# d- 
numero1 = 10
# dad0 = int(input(Digite o numero que deseja: )) # Faltou o uso de aspas em volta do texto input
print(numero1 * dado)
numero1 = 10
dado = int(input('Digite o numero que deseja: '))
print(numero1 * dado)
