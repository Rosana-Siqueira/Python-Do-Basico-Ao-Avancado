# Criar um arquivo de texto, inserir o lucro mensal de uma startup entre os meses de janeiro e maio, informando o mês e o valor, através da entrada do usuário. 
# Após isso, ler o arquivo e imprimir o mês de maior lucro.

with open('ExercíciosEscreverEmArquivos.txt', 'w') as LE:
    while True:
        mes = input('Mês: ')
        if mes == 'sair':
            break
    else:
        LE.write(f'{mes} ') 
        LE.write(input('Lucro: '))
        LE.write('\n')

relatorio = {}

with open('ExercíciosEscreverEmArquivos.txt') as LE:
    for linha in LE:
        relatorio[linha[0:3]] = int(linha[4:]) 
        
print(relatorio)
maiorLucro = 0
mesMaiorLucro = 0

for mes, lucro in relatorio.items():
    if lucro > maiorLucro:
        maiorLucro = lucro
        mesMaiorLucro = mes

print(f'Mês com maior lucro: {mesMaiorLucro} com {maiorLucro} reais')
