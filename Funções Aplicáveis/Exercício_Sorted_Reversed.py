# Receba números inteiros do usuário e armazene-os em uma lista. 
# Crie uma condição para o número 0 finalizar o processo de preenchimento.
# Após isso, imprima o maior valor da lista utilizando as funções sorted() e len().
# Por fim, utilize reversed() para inverter a lista e obtenha, pelo índice, o valor intermediário da mesma.
# Obs.: Caso o número de valores da lista seja par, pegue a média dos dois valores centrais.

numeroInt = 1
listaNumeros = []

while numeroInt != 0:
    numeroInt = int(input('Digite um número inteiro: '))
    if numeroInt != 0:
        listaNumeros.append(numeroInt)

ordenada = sorted(listaNumeros) #Ordena a lista 'listaNumeros'
tamanho = len(listaNumeros) #Obtém o tamanho da lista 'listaNumeros'

print(f'Maior valor: {ordenada[tamanho - 1]}') #0 -1 é porque o len retorna a quantidade de elementos da lista, ou
#seja, começando do 1 até o último elemento. Mas os índices começam do 0, então, o último é o tamanho da lista -1.

invertida = reversed(ordenada) #Inverte a lista
listaInvertida = list(invertida)

if tamanho % 2 == 1:
    print(f'Valor intermediário: {listaInvertida[tamanho // 2]}')
else:
    print(f'Valor intermediário: '
    f'{(listaInvertida[tamanho // 2] + listaInvertida[(tamanho // 2) - 1]) / 2}')
    