# Faça um programa que contabiliza time de heróis e vilões da seguinte forma:

# - Crie um dicionário chamado herói com chave sendo o nome do personagem e o elemento o nível de poder do personagem entre 1 a 100. Ex.: herói = {'Flash':85}
# - Crie outro dicionário que serão as armas que podem ser usados pelo herói, sendo a chave o nome da arma e o elemento o nível de poder de 0 a 100. Ex.: arma = {'Escudo do Capitão América':60}
# - Crie um último dicionário representando os vilões sendo a chave o nome e o elemento o nível de poder de 0 a 200.
# Ex.: vilao = {'Thanos':175}
# Após isso o usuário poderá escolher um herói, uma arma soma os pontos de poder e escolher um vilão para lutar, apresente quem foi o vencedor, caso for o herói imprima a arma usada. Caso resulte em empate informe na saída.
# Observação: Pode definir qualquer herói, vilao e arma que quiser.

herois = {'Capitão América':75,'Hulk':100,'Pantera Negra':80,'Homem de Ferro':60,'Thor':85,}
armas = {'Escudo do Capitão América':65,'Ficar verde':90,'Armadura Pantera': 70,'Armadura Homem de Ferro': 50,
    'Machado Thor': 75,}
viloes = {'Thanos':180,'Godzila': 140,'Ultron': 120,'Venom': 160,'Look':200,}

heroi_escolhido = input('Digite o herói escolhido: ')
arma_escolhida = input('Digite a arma escolhida: ')
vilao_escolhido = input('Digite o vilão escolhido: ')

nivel_poder_heroi_arma = herois[heroi_escolhido] + armas[arma_escolhida]

if nivel_poder_heroi_arma > viloes[vilao_escolhido]:
    print(f'O vencedor é {heroi_escolhido} com {arma_escolhida}')
elif nivel_poder_heroi_arma == viloes[vilao_escolhido]:
    print(f'Deu empate')
else:
    print(f'O vencedor é {vilao_escolhido}! Terra em Perigo!')
