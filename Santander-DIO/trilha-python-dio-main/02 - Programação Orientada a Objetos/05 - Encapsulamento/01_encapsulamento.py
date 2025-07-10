class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # privado
        self.nro_agencia = nro_agencia # publico

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
print(conta._saldo) #ERRADO. NÃO SE DEVE FAZER O ACESSO A UMA PROP. PRIVADA DIRETAMENTE.
conta.depositar(100)

print(conta.nro_agencia)
print(conta.mostrar_saldo())

#Como fazer de forma correta o acesso a uma variável privada? O acesso deve ser feito pelo MÉTODO.