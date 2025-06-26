# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    entrada = input().strip()  
    partes = entrada.split(',')

    nome = partes[0].strip()
    tema = partes[1].strip()

    if tema not in eventos:
        eventos[tema] = []

    eventos[tema].append(nome)
   

for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")