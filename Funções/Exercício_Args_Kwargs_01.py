# Faça o sistema de uma corrida entre MerCúrio, Papa-Léguas, SoNic, FlaSh, LiGeirinho e Super Homem (MC, PL, SN, FS, LG, SH).
# Crie uma função que receba os 6 corredores em ordem do vencedor até o último (pedir para o usuário), sendo os três primeiros em variáveis obrigatórias e os três últimos em kwags, com as chaves sendo as posições na corrida.
# Pedir ao usuário se houve trapaça:
# - se não houve: apresentar a classificação final.
# - se houve: pedir ao usuário quem trapaceou e quem foi prejudicado. Depois, trocá-los de posições. 
# Por fim, apresentar a classificação final.

def classParcial(primeiro, segundo, terceiro, **outros):
    op = input('Houve trapaça? s/n: ')
    quarto = ''
    quinto = ''
    ultimo = ''
    if op == 'n':
        for posicao, corredor in outros.items():
            if posicao == '4':
                quarto = corredor
            elif posicao == '5':
                quinto = corredor
            elif posicao == '6':
                ultimo = corredor

        classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo)
    elif op == 's':
        colocacao = [primeiro, segundo, terceiro]
        colocacao.extend(outros.values())

        babaca = input('Quem trapaceou?: ')
        vitima = input('Quemm foi prejudicado?: ')

        posBabaca = colocacao.index(babaca)
        posVitima = colocacao.index(vitima)

        colocacao[posBabaca] = vitima
        colocacao[posVitima] = babaca

        classFinal(*colocacao)

    else:
        print('Digite uma opção válida!')

def classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo):
    print('Classificação final: ')
    print(f'Primeiro: {primeiro}')
    print(f'Segundo: {segundo}')
    print(f'Terceiro: {terceiro}')
    print(f'Quarto: {quarto}')
    print(f'Quinto: {quinto}')
    print(f'Último: {ultimo}')

print('Corredores: ')
print('Mercúrio (MC), Papa-Léguas (PL), Sonic (SN), Flash (FS), Ligeirinho (LG), Super Homem (SH)')

pri = input('Vencedor: ')
seg = input('Segundo: ')
ter = input('Terceiro: ')
qua = input('Quarto: ')
qui = input('Quinto: ')
ult = input('Último: ')

outros = {'4':qua, '5':qui, '6':ult}

classParcial(pri, seg, ter, **outros)
