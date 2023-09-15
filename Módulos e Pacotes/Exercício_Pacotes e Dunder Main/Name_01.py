# Crie uma pasta, uma subpasta e em seguida um módulo na subpasta contendo uma função qualquer. 
# Acesse o módulo no programa principal e execute a função.
# OBS.: No módulo criado, estabeleça uma condição para a função ser acessada se o módulo for importado e executado em outro. Ou seja, quando o módulo em questão não é o principal (main).

from PacoteFora.PacoteDentro.MóduloDentro import preverFututo
from random import choice as ch

idade = [12, 65, 87, 14, 52, 42, 4, 84, 14, 73, 16, 61, 34, 28, 35, 22]
formacao = ['filosofia', 'engenharia', 'medicina', 'artes', 'letras', 'biologia']
trabalho = ['bartender', 'politico(a)', 'administrador(a)', 'professor(a)', 'carpinteiro(a)']
pais = ['França', 'Angola', 'Escócia', 'Espanha', 'Turquia']
animal = ['crocodilo', 'urso', 'sapo', 'elefante', 'tubarão', 'golfinho']
nome = [input('Digite um nome: ')]

preverFututo(nome, ch(idade), ch(formacao), ch(trabalho), ch(pais), ch(animal))
