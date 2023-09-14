# Chegou o famoso dia dos namorados, Mateus deixou para decidir o presente em cima da hora. Ele resolveu comprar um tipo de flor, um presente e escolher um lugar para saírem, ele anotou todas as opções abaixo:
#       Flores
# Tipo             Preço
# Rosas Vermelhas  145.00
# Girassóis        125.00
# Margaridas       120.00
# Flores do campo  140.00

#      Presente

# Tipo              Preço
# Urso de Pelúcia   55.00
# Caixa de Bombom   60.00
# Colar             75.00
# Roupas            40.00

#       Lugar

#Tipo                 Preço
# Praia               70.00
# Sair para jantar    150.00
# Parque de diversões 120.00
# Hotel               180.00

# - Crie um programa que descubra qual a combinação mais cara, em seguida mais barata e a média opção. Imprima a combinação em cada caso.
# - use um dicionário para cada item (flor, lugar e presente)

flores = {'Rosas Vermelhas':145, 'Girassóis':125, 'Margaridas':120, 'Flores do campo':140}
presentes = {'Urso de Pelúcia':55, 'Caixa de Bombom':60, 'Colar':75, 'Roupas':40}
lugares = {'Praia':70, 'Sair para jantar':150, 'Parque de diversões': 120, 'Hotel':180}

preco_total = 0
flor_cara = ' '
presente_caro = ' '
lugar_caro = ' '

for flor,valor in flores.items():
    for presente,preco in presentes.items():
        for lugar, custo in lugares.items():
            preco_atual = valor + preco + custo
            if preco_atual > preco_total:
                preco_total = preco_atual
                flor_cara = flor
                presente_caro = presente
                lugar_caro = lugar

print(f'Custo total: {preco_total}, Flor: {flor_cara}, Presente: {presente_caro}, Lugar:{lugar_caro}')

aux = 0
preco_total = 0
flor_barata = ' '
presente_barato = ' '
lugar_barato = ' '

for flor,valor in flores.items():
    for presente,preco in presentes.items():
        for lugar, custo in lugares.items():
            if aux == 0:
                preco_total = valor + preco + custo
                aux += 1
            else:
                preco_atual = valor + preco + custo
                if preco_atual < preco_total:
                   preco_total = preco_atual
                   flor_barata = flor
                   presente_barato = presente
                   lugar_barato = lugar

print(f'Custo total: {preco_total}, Flor: {flor_barata}, Presente: {presente_barato}, Lugar:{lugar_barato}')

preco_total = 0
list = []

for flor,valor in flores.items():
    for presente,preco in presentes.items():
        for lugar, custo in lugares.items():
            list.append(valor + preco + custo)
list.sort() # Organiza a lista do menor para maior elemento
preco_total = list[len(list) // 2]

for flor,valor in flores.items():
    for presente,preco in presentes.items():
        for lugar, custo in lugares.items():
            if valor + preco + custo == preco_total:
                print(
                    f'Custo total: {preco_total}, Flor: {flor}, Presente: {presente}, Lugar:{lugar}')
                
