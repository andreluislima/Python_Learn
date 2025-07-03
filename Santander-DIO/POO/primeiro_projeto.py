"""
João tem uma bicicletaria e gostaria de registrar as vendas e suas bicicletas.
Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos.
"""

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Plim plim...")
        
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada")
        
    def correr(self):
        print("Vruuuuuuummmm...")
        
    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"
        
    # def __str__(self):
    #     return f"{self.__class__.__name__}"
    
    # def __str__(self):
    #     return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"
    
    # Representação dinamica da classe. Se um atributo for adicionado esse metodo reflete aumtomaticamente as mudanças.
    def __str__(self):
        return f"{self.__class__.__name__}: {', ' .join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelho", "caloi", 2022, 700)
print(b1)

# b1.buzinar()
# b1.correr()
# b1.parar()

# print(b1.cor, b1.ano, b1.valor)


# Observações
"""
sef -> Ref. explicita. Em outras linguagens essa referencia é implicita.

"""

## Exibindo os valores da classe


