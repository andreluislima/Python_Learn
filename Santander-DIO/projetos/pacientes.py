# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Entrada dos dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# Função que organiza os pacientes por prioridade
def organizar_atendimento(pacientes):
    urgentes = []
    idosos = []
    demais = []

    for paciente in pacientes:
        nome, idade, status = paciente

        if status.lower() == "urgente":
            urgentes.append(nome)
        elif idade >= 60:
            idosos.append(nome)
        else:
            demais.append(nome)

    # Ordena os nomes por idade decrescente, sem mudar a estrutura
    urgentes = sorted(urgentes, key=lambda nome: next(idade for n, idade, status in pacientes if n == nome), reverse=True)
    idosos = sorted(idosos, key=lambda nome: next(idade for n, idade, status in pacientes if n == nome), reverse=True)
    demais = sorted(demais, key=lambda nome: next(idade for n, idade, status in pacientes if n == nome), reverse=True)

    return urgentes + idosos + demais

# Gera a ordem de atendimento
ordem_atendimento = organizar_atendimento(pacientes)

# Exibe o resultado
print("Ordem de Atendimento:", ", ".join(ordem_atendimento))
