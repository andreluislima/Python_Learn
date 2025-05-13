from adodbapi.is64bit import Python


# Em python, usamos a palavra reservada 'class' para definirmos uma class
# Utilizamos 'pass' quando temos um bloco de codigo que ainda nao está implementado.

class Lampada:
    pass

class ContaCorrente:
    pass

# Declaracao de uma classe com atributos em Java
# public class Lampada(){
#
#     private int voltagem;
#     private string cor;
#     private boolean ligada = false;

# public Lampada(int voltagem, String cor){
#     this.voltagem = voltagem
#     this.cor = cor;
# }
# }

# Declaracao de uma classe com atributos em Python
class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

# DIFERENÇAS
# Os modificadores de acesso em Java são substituidos por '__' em Python()
# Os atributos não são declarados na classe mas no metodo construtor.

class Produto:
    imposto = 1.05

    def __init__(self, nome, descricacao, valor):
        self.nome = nome
        self.descricacao = descricacao
        self.valor = (valor + Produto.imposto)

p1 = Produto('Playstation 5', 'Video Game', 4500)
p2 = Produto('Playstation 5', 'Video Game', 5000)

print(p1.valor)
print(p2.valor)




