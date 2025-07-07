
saldo = 0.0
extrato = []
real = "R$ "
numero_saques = 0



def menu():
    msg_boas_vindas = ("\nBem-Vindo ao Banco SantANDRÉ.\n>>O SEU banco<<\n"
    "Acesse o menu e escolha o que você irá fazer")

    opcoes =  """
            [1] -> Depósito
            [2] -> Saque
            [3] -> Extrato
            [4] -> Avaliar Sistema
            [0] -> Sair
        """
    aviso = ("Aviso!\nUse apenas NÚMEROS para acessar o sistema.")

    return msg_boas_vindas, opcoes, aviso

msg, opcoes, aviso = menu()
print(msg)
print(opcoes)
print(aviso)

def deposito(saldo, extrato):

    print("\n### DEPÓSITO ###")
    valor = float(input("Faça o seu depósito: "))

    while(valor <= 0):
        valor = float(input("Valor inválido! Insira um número inteiro maior que Zero: "))
    saldo += valor

    extrato.append(f'Depósito {real}{valor:.2f}')
    print(f'Depósito realizado com sucesso!\nSeu saldo atual é: {real}{saldo:.2f}')
    return saldo, extrato

def saque(*,saldo, extrato, valor_limite_saques=500, numero_saques, limite_saques=3):

        print("\nVocê selecionou a opção: 2 -> Saque")
        print("\n### SAQUE ###")  

        if numero_saques >= limite_saques:
            print("\nVocê excedeu o limite diário de saques.")
            return saldo, extrato, numero_saques


        valor = float(input("Informe a quantia que deseja sacar: "))
        
        if(valor > saldo):
            print(f"\nSaldo insuficiente! Você tentou sacar {real}{valor:.2f}, mas seu saldo é {real}{saldo:.2f}")
        elif(saque > valor_limite_saques):
            print(f'\nLimite do saque excedido! Você tentou sacar {real}{valor:.2f}, mas o permitido é no máximo {real}500,00')
        else:
            saldo -= valor
            numero_saques += 1
            extrato.append(f'Saque {real}{valor:.2f}')
            
            print(f"Saque realizado com sucesso! Saldo atual: {real}{saldo:.2f}")
            print(f"Número de saques realizados: {numero_saques}")

        return saldo, extrato, numero_saques
                   

while True:
    menu()

    opcao = int(input ("\nSelecione uma opção válida para o menu: "))

    if(opcao == 1):
    #     saldo, extrato = deposito(saldo, extrato)
    # print(f'Saldo:{saldo}\nExtrato:{extrato}')
        deposito(saldo, extrato)

    elif(opcao == 2):
        saque(
            saldo=saldo,
            extrato=extrato,
            numero_saques=numero_saques
        )

            
