# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0


# Entrada do número de itens
n = int(input("Quantos itens deseja adicionar ao carrinho? ").strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input("Digite o nome do produto e o preço (ex: Pão 3.50): ").strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

for produto, preco in carrinho:
    print(f"{produto}: R${preco:.2f}")

print(f"Total: R${total:.2f}")

