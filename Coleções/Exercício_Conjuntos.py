# ami e Dudu irão fazer uma competição de quem visita mais Estados no Brasil em um período de 6 meses, até então Dudu já visitou o Espírito Santo e São Paulo, enquanto Sami visitou Rio de Janeiro e Bahia. Crie dois conjuntos diferentes para simbolizar os estados que cada um foi. Após 6 meses Dudu visitou Bahia, Acre, Santa Catarina e Sergipe, enquanto Sami visitou Bahia, Minas Gerais, Amazonas e Paraná, atualize cada um dos conjuntos com os novos Estados. Responda:

# - Quais Estados Dudu visitou que Sami não foi?
# - Quais Estados ambos foram?
# - Sendo 27 Estados no Brasil todo, qual porcentagem o vencedor visitou?

estado_sami = {'RJ','BA'}
estado_dudu = {'ES','BA'}

sair = ''
while sair != 'nao':
    estado_sami.add(input('Qual Estado Sami visitou a mais? '))
    sair = input('Tem mais Estados a adicionar? ')

sair = ''
while sair != 'nao':
    estado_dudu.add(input('Qual Estado Dudu visitou a mais? '))
    sair = input('Tem mais Estados a adicionar? ')

print(estado_dudu.difference(estado_sami))
print(estado_sami.intersection(estado_dudu))

if len(estado_sami) > len(estado_dudu):
    print(f'Sami ganhou e visitou {len(estado_sami)*100 // 27}%')
elif len(estado_dudu) > len(estado_sami):
    print(f'Dudu ganhou e visitou {len(estado_dudu)*100 // 27}%')
else:
    print(f'Deu empate e ambos visitaram {len(estado_dudu)*100 // 27}%')
    