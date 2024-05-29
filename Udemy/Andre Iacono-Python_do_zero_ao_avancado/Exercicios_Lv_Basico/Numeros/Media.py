# Média

"""
Desenvolva um programa que leia quatro notas e que apresente a média final

"""

# print('Digite 4 números\n')
#
# # - Modo 1
# numero_1: float = float(input('#1 - Digite um número: '))
# numero_2: float = float(input('#2 - Digite um número: '))
# numero_3: float = float(input('#3 - Digite um número: '))
# numero_4: float = float(input('#4 - Digite um número: '))
#
# media: float = (numero_1 + numero_2 + numero_3 + numero_4)/4

# modo 2

valor = 0
for i in range(4):
    numero: float = float(input('Digite numero: '))
    print(f'#{i+1} | {numero}')
    valor += numero

    # print(valor)

print(f'\nMédia: {valor/4}')

print(f'\nMédia: {(valor/4):.2f}')
