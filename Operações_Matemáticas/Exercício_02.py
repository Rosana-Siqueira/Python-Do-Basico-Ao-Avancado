# Converter uma temperatura de graus ºC para ºF e para K.
# Dados: ºF = ºC * 1.8 * 32, K = ºC + 273.15

tempC = float(input('Temperatura em ºC: '))
tempF = tempC * 1.8 + 32
print(f' A temperatura em ºF é: {tempF}ºF\n')

tempC = float(input('Temperatura em ºC: '))
tempK = tempC + 273.15
print(f'A temperatura em ºK é: {tempK}')
