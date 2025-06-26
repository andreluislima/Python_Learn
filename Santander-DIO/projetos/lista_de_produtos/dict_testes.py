# pessoa = {"nome":"Ana", "idade":20}
# pessoas = [
     
#     {"nome": "Ana", "idade": 20},
#     {"nome": "Lua", "idade": 31},
#     {"nome": "Bia", "idade": 24},
#     {"nome": "Marcos", "idade": 11}
# ]

# print(pessoa.get("nome"))
# print(pessoa.get("idade"))
# print("\n##########\n")

# for p in pessoas:
#     print(f'Nome: {p["nome"]}, Idade: {p["idade"]}') 

# print("\n##########\n")

# eventos = []

# n = int(input("Número de participantes no evento: "))

# for _ in range(n):
#     nome = input("Nome: ")
#     contato = input("Contato: ")
    
#     participante = {
#         "nome": nome,
#         "contato": contato
#     }
    
#     eventos.append(participante)   

# # Agora sim!
# print("\nLista de Participantes:")
# for p in eventos:
#     print(f"Nome: {p['nome']}, Contato: {p['contato']}")

print("\n##########\n")

eventos = {}

# n = int(input("Número de participantes no evento: "))

for _ in range(2):
    nome = input("Nome: ")
    contato = input("Contato: ")

    eventos[nome] = contato


for a, b in eventos.items():
    print(a, b)

print(eventos[nome])