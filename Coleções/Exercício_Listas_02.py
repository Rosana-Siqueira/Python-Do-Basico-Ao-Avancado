# Criar um sistema de comando de uma loja de jogos. O programa deve conter pelo menos 6 listas:
# 1 indicando quais jogos estão disponíveis para venda. 2 para mostrar o preço de cada jogo. 3 para mostrar a quantidade de jogos disponíveis na loja para venda. 4 informando o preço de fábrica dos jogos para aumentar o estoque. 5 para registrar as vendas. 6 para registrar as compras de estoque.
# Todas as informações de um jogo devem estar ao mesmo índice nas listas.
# criar um menu interativo com as seguintes opções para o usuário: Registrar venda, Compra de estoque, Resumo da loja, Sair.
# Ao sair indicar que o caixa está fechado. O usuário deve controlar o sistema da loja, registrando as vendas e as compras de estoque, sem esquecer de alterar os valores da lista de quantidade.

jogos = ['Gow', 'Minecraft', 'GTA', 'Sonic', 'FIFA']
precosVenda = [210.00, 2.99, 150.00, 1.00, 125.00]
precosCompraEstoque = [105.00, 1.50, 75.00, 0.90, 62.50]
quantidade = [3, 0, 2, 5, 1]
vendas = []
compraDeEstoque = []

op = 0

while op != 4:
    print('1 - Registrar venda\n2 - Compra de estoque\n3 - Resumo da loja\n4 - Sair')
    op = int(input('Opção: '))

    if op == 1:
        jogoVendido = input('Jogo vendido: ')
        quantidadevendida = int(input('Quantidade vendida: '))
        if quantidadevendida <= quantidade[jogos.index(jogoVendido)]:
            print(f'{jogoVendido} Vendido!')
            quantidade[jogos.index(jogoVendido)] -= quantidadevendida
            vendas.append(precosVenda[jogos.index(jogoVendido)] * quantidadevendida)

        else:
            print('\nNão há essa quantidade disponível em estoque\n')

    elif op == 2:
        jogoComprado = input('Jogo comprado: ')
        quantidadeComprada = int(input('Quantidade comprada: '))
        print(f'\n{jogoComprado} comprado!')
        quantidade[jogos.index(jogoComprado)] += quantidadeComprada
        compraDeEstoque.append(precosCompraEstoque[jogos.index(jogoComprado)] * quantidadeComprada)

    elif op == 3:
        print('\n\nQuantidade de jogos em estoque: ')
        for jogo in jogos:
            print(f'{jogo}: {quantidade[jogos.index(jogo)]}')
        print(f'Lucros: R$ {sum(vendas)}')
        print(f'Despesas: R$ {sum(compraDeEstoque)}')
        print(f'Caixa: R$ {sum(vendas) - sum(compraDeEstoque)}')

print('\n\nCaixa Fechado!')



