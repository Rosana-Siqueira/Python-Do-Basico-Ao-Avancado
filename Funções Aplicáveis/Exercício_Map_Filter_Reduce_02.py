# Realizar o calculo do IMC através de uma função utilizando map com os dados fornecidos abaixo sobre peso e altura, e salvar os resultados em outra lista.
# Após isso, aplicar o filter para separar pessoas obesas (IMC > 25).

# Dados:
# indice 0 das tuplas: peso (kg)
# indice 1 das tuplas: altura (m)
# listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (56, 1.56), (69, 1.76), (112, 1.63), (98, 1.59)]

listaAmostras = [(62, 1.73), (90, 1.86), (76, 2.12), (56, 1.56), (69, 1.76), (112, 1.63), (98, 1.59)]

def calculoIMC(amostra):
    imc = amostra[0] / (amostra[1] ** 2)
    return imc

imc = map(calculoIMC, listaAmostras)

resultadoIMC = list(imc)
resultIMC = []

for num in resultadoIMC:
    resultIMC.append(round(num))

print(resultIMC)

sobrepeso = filter(lambda imc: imc > 25, resultIMC)
print(f'IMCs acima do peso: {list(sobrepeso)}')
