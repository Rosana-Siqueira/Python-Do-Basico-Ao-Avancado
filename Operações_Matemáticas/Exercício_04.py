# Criaçao de personagem de mndo de ficao, apresentando opcoes de acordo com os tipos das variáveis:
# - Cor de cabelo(string)
# - Cor de pele(string)
# - Classe: Guerreiro, Mago, Arqueiro(sting)
# - Idade(int)
# - Altura(flooat)
# - Habilidade Especifica(sting)
# Imprima para o usário o personagem completo.


print('----------Bem vindo a um novo universo----------')
print('--------------Crie seu personagem---------------')
cor_cabelo = input('Digite a cor do cabelo: ')
cor_pele = input('Digite a cor da pele: ')
classe = input('Digite a sua classe dentre: 1- Guerreiro\n2 - Mago\n3 - Arqueiro\nOpcao: ')
idade = int(input('Digite sua idade em anos: '))
altura = float(input('Digite sua altura em metros: '))
habilidade_especifica = input('Digite sua habilidade: ')
print('----------------Personagem Criado---------------')
print(f'Seu personagem tem: \n'
      f'Cabelo de cor: {cor_cabelo}\n'
      f'Pele de cor {cor_pele}\n'
      f'Classe {classe}\n'
      f'Idade de {idade}\n'
      f'Altura de {altura}\n'
      f'Habilidade de {habilidade_especifica}')
