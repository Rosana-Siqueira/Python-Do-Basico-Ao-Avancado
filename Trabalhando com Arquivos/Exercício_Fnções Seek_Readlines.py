# Crie um arquivo com conteúdo aleatório. 
# Em seguida, abra o arquivo, leia-o 3 vezes a partir dos caracteres 5, 9, 14. Por fim, feche o arquivo.

arquivo = open('Cores.txt')

arquivo.seek(5)
print(f'\n\n{arquivo.read()}')

arquivo.seek(9)
print(f'\n\n{arquivo.read()}')

arquivo.seek(14)
print(f'\n\n{arquivo.read()}')

arquivo.close()
