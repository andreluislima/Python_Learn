class Veiculo:
    def  __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando motor...")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")
        
    def __str__(self):
        return self.cor


moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

caminhao01 = Caminhao("branco", "xyz-009", 4, False)
caminhao01.esta_carregado()

print(caminhao01)


"""
    Sobrescrever o método ou uma implementação.
    
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    Super chama a implementação da classe pai.
"""