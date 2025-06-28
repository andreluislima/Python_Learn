# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

if cupom in descontos:
    desconto = descontos[cupom]
    preco_final = preco * (1 - desconto)
    print(f'{preco_final:.2f}')
else:
    print("cumpom inválido")
  
# TODO: Aplique o desconto se o cupom for válido:

# Dado de entrada:
# 100
# DESCONTO10
# Saída esperada:
# 90.00