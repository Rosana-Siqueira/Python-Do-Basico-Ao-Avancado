# Crie 3 listas: uma com o nome de 3 companhias aéreas, e as outras duas representando o número de passageiros por companhia em dois voos: voo1 e voo2. Utilize zip(), lambda e map() para obter o valor máximo de passageiros por companhia nos dois voos e associar estes valores com o nome das companhias, formando uma lista de tuplas.
# Por fim, utilizar filter() e lambda para determinar a classificação da companhia, conforme indicado nos dados abaixo.
# Dados:
# 0 < Passageiros < = 100: 1 estrela.
# 100 < Passageiros < = 200: 2 estrela.
# 200 < = Passageiros < = 300: 3 estrelas.

companhias = ['GOL', 'LATAM', 'AZUL']
voo1 = [115, 95, 110]
voo2 = [195, 80, 225]

voo1e2 = zip(voo1, voo2) #Junta os números de passageiros de cada companhia
maxPass = map(lambda voos: max(voos), voo1e2) #Determina o valor maz de passageiros por campanhia entre os voos 1 e 2
listamaxPass = list(maxPass)

compMax = zip(companhias, listamaxPass)
listacompMax = list(compMax)

umaEst = list(filter(lambda valMax: valMax[1] < 100, listacompMax)) #Filtra a companhia aérea que menos de 100
#passageiros em seu valor máximo e depois converte o resultado para uma lista.
duasEst = list(filter(lambda valMax: valMax[1] > 100 and valMax [1] <= 200, listacompMax))
tresEst = list(filter(lambda valMax: valMax[1] > 200 and valMax [1] <= 300, listacompMax))

print(f'Uma estrela: {umaEst[0][0]} - Max Passageiros: {umaEst[0][1]}')
print(f'Duas estrelas: {duasEst[0][0]} - Max Passageiros: {duasEst[0][1]}')
print(f'Tres estrelas: {tresEst[0][0]} - Max Passageiros: {tresEst[0][1]}')
