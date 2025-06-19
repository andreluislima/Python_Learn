MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade")

if idade < MAIOR_IDADE:
    print("Menor de idade")


saldo = 2400.00
saque = 3200.00

status = "Sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque!")
 