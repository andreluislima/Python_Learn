class Biblioteca:
    nome = ""
    ativo: False

biblioteca_cidade = Biblioteca()
biblioteca_estado = Biblioteca()

bibliotecas = [biblioteca_estado, biblioteca_cidade]
print(bibliotecas)

for biblioteca in bibliotecas:
    print(vars(biblioteca))