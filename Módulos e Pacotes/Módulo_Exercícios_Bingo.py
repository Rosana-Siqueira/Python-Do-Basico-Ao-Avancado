from random import choice as ch
def sorteio(cartela1, cartela2, max):
    numSorteados = []
    numerosIniciais1 = []
    numerosIniciais2 = []
    vencedor = ''
    sorteador = list(range(1, max + 1))
    while vencedor == '':
        numS = ch(sorteador)
        sorteador.pop(sorteador.index(numS))
        numSorteados.append(numS)
        if numS in cartela1:
            numerosIniciais1.append(cartela1.pop(cartela1.index(numS)))
            if len(cartela1) == 0:
                vencedor = 'João'
                print(f'Vencedor: {vencedor}')
                print(f'Cartela: {numerosIniciais1}')
        if numS in cartela2:
            numerosIniciais2.append(cartela2.pop(cartela2.index(numS)))
            if len(cartela2) == 0:
                vencedor = 'Maria'
                print(f'Vencedor: {vencedor}')
                print(f'Cartela: {numerosIniciais2}')
    print(f'Números sorteados: {numSorteados}')


