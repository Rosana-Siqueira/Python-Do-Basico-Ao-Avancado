# Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira, potência). Peça a operação desejada e depois os dois números ao usuário.

print('1 - Soma\n2 - Multiplicação\n3 - Divisão Inteira\n4 - Potência')
op = int(input('Escolha uma operação: '))
num1 = float(input('Digite primeiro número: '))
num2 = float(input('Digite segundo número: '))

if op == 1:
    print(f'Soma: {num1 + num2}')
elif op == 2:
    print(f'Multiplicação: {num1 * num2}')
elif op == 3:
    print(f'Divisão Inteira: {num1 // num2}')
elif op == 4:
    print(f'Potência: {num1 ** num2}')
else:
    print('Digite uma opção válida!')
    