def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # Listas para armazenar o resultado
    confirmadas = []
    recusadas = []

    # Verifica se cada reserva pode ser confirmada com base na disponibilidade dos quartos
    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            confirmadas.append(reserva)
            quartos_disponiveis.remove(reserva)  # Remove o quarto para evitar reserva duplicada
        else:
            recusadas.append(reserva)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()
