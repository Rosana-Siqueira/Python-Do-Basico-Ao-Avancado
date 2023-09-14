# Faça o debug a partir da primeira linha (x = 1) com o próprio Pycharm ou método pdb (Breakpoint) do seguinte código e anote os valores das variáveis em cada linha como resposta.

x = 1
y = 10
z = 100
x = x + (y + z) //2
y = y ** 2 + z * x
z = (z ** 2) + z + x
soma = x + y + z
print(soma)

# 1º Linha = vazia

# 2º Linha = x = 1

# 3º Linha = x = 1
# y = 10

# 4º Linha = x = 1
# y = 10
# z = 100

# 5º Linha = x = 56
# y = 10
# z = 100

# 6º Linha = x = 56
# y = 5700
# z = 100

# 7º Linha = x = 56
# y = 5700
# z = 10156

# 8º Linha = x = 56
# y = 5700
# z = 10156
# soma = 15912

