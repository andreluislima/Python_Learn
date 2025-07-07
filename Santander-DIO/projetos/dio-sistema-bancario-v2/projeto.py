
deposito = 0.0
saldo = 0.0
saldo += deposito
saque = 0.0
real = "R$ "
dolar = "$ "
tentativas = 0

msg_boas_vindas = "\nBem-Vindo ao Banco SantANDRÉ.\n>>O SEU banco<<"
msg_menu = "Acesse o menu e escolha o que você irá fazer"
menu =  """
            [1] -> Depósito
            [2] -> Saque
            [3] -> Extrato
            [4] -> Avaliar Sistema
            [0] -> Sair
        """
aviso = ("\nAviso!\nUse apenas NÚMEROS para acessar o sistema.")

opcao = None
avalicacao = 0


print(msg_boas_vindas)
print(msg_menu + "\n" + menu)
print(aviso)


while True:
    opcao = int(input ("\nSelecione uma opção válida para o menu: "))
    if(opcao == 1):
        print("\nVocê selecionou a opção: 1 -> Depósito")
        print("\n### DEPÓSITO ###")
        deposito = float(input("Faça o seu depósito: "))
        while(deposito <= 0):
            deposito = float(input("Valor inválido! Insira um número inteiro maior que Zero: "))
        else:
            saldo += deposito
            print("Depósito realizdo com sucesso!")
            print(f'\nSeu saldo atual é: {real}{saldo:.2f}')
            print(menu + aviso)

    elif(opcao == 2):
        print("\nVocê selecionou a opção: 2 -> Saque")
        print("\n### SAQUE ###")    
            
        for tentativas in range(3):

            saque = float(input("Informe a quantia que deseja sacar: "))
            if(saque > saldo):
                print(f"\nSaldo insuficiente! Você tentou sacar {real}{saque:.2f}, mas seu saldo é {real}{saldo:.2f}")
            elif(saque >500):
                print(f'\nLimite do saque excedido! Você tentou sacar {real}{saque:.2f}, mas o permitido é no máximo {real}500,00')
            else:
                saldo -= saque
                print(f'\nSaque realizado com sucesso!\nSeu saldo atual é: {real}{saldo:.2f}')
                print(f'\nNúmero de saques: {tentativas + 1}')
                print(menu + aviso)
        else:
            print("\nVocê execedeu o limite diário de saques que é de 3 por dia")
            print(menu + aviso)

    elif(opcao == 3):
        print("\nVocê selecionou a opção: 3 -> Extrato")
        print(f'\n### EXTRATO ###\nSaldo: {real}{saldo:.2f}')
    
    elif(opcao == 4):
        print("\nVocê selecionou a opção: 4 -> Avaliação")
        print("\n### AVALIAÇÃO ###\nE aí? O que achou do nosso sistema?\nDeixe uma avaliação!")

        avalicacao = int(input("Escolha 0 para muito bom! ou 10 para excelente!: "))

        print(f'\nSua escolha foi: {avalicacao}\n Muito obrigado por usar o banco SantANDRÉ')
        print("\n...Saindo do sistema...")
        break

    elif(opcao == 0):
        print("\nVocê selecionou a opção 0 -> Sair")
        print("\n...Saindo do sistema...")
        print("Muito obrigado por usar o banco SantANDRÉ")
        break

    else:
        opcao = int(input ("Selecione uma opção válida para o menu: "))