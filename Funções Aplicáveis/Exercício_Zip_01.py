# Está acontecendo uma gincana na Escola e você foi escolhido(a) para realizar o controle da pontuação! 
# Para isso, crie 4 listas (1 com nome das pessoas que participam da gincana.
# As outras 3 cada uma representam uma prova armazenam valores de 0 a 100, ou seja, as notas que cada participante obteve. 
# Por fim, utilize zip() para retornar um dicionário com o nome de cada aluno como chave e o somatório de suas notas em cada prova como valor. 
# Após isso, imprima o participante vencedor.

nomes = ['Maria Joaquina', 'Dom Pedro', 'Napoleão', 'Chaves', 'Jhennifer Lopez']
provaCorrida = [2, 7.5, 9, 8.67, 6.8]
provaEscalada = [1, 8, 4, 6.3, 9.1]
provaOperMatem = [0, 8.7, 5.8, 10, 4.3]

listaNotas = []

tabela = zip(provaCorrida, provaEscalada, provaOperMatem)
for notas in tabela:
    listaNotas.append(sum(notas))

tabelaFinal = zip(nomes, listaNotas)

dicioFinal = dict(tabelaFinal)

vencedor = ''
pontos = 0

for part, pts in dicioFinal.items():
    print(f'Participante: {part}. Pontos: {pts}')
    if pts > pontos:
        pontos = pts
        vencedor = part

print(f'\n____Vencedor: {vencedor} - Pontos: {pontos}____')

