# Crie duas listas, uma para carrinho do supermercado que irá receber produtos comprados e outra para os preços dos produtos. Utilizando um loop, preencha as listas com 5 produtos e 5 preços, recebendo estes dados do usuário (input). Por fim, some os preços, imprima o valor total e os produtos do carrinho.

listaCarrinho = [] 
listaPrecos = [] 
contProdutos = 0 
valorTotal = 0
produto = ''

while contProdutos < 5: 
    produto = input('Produto: ')
    listaCarrinho.append(produto) 
    preco = float(input('Preço: '))
    listaPrecos.append(preco)
    contProdutos += 1

for id in range(0, 5): 
    valorTotal += listaPrecos[id] 


print(f'Produtos comprados: {listaCarrinho}')
print(f'Valor total: R$ {valorTotal}')
