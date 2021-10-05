
lista = []
def remove_repetidos(lista):
    lista2 = []
    for n in lista:
        if n not in lista2:
            lista2.append(n)
    return sorted(lista2)

print(remove_repetidos(lista))
