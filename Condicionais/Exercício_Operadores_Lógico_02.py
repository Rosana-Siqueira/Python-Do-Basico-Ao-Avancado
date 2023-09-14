# Crie um programa que encontre e imprima as raízes de uma equação do segundo grau, utilizando o método de Bhaskara.

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = (b ** 2) - (4 * a * c) 

x1 = (-b + delta ** 0.5) / (2 * a) 
x2 = (-b - delta ** 0.5) / (2 * a)

print(f'As raizes são: {x1} e {x2}')
