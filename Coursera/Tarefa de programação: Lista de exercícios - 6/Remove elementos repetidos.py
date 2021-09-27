''''''
'''
Exercício 1 - Removendo elementos repetidos

Escreva a função remove_repetidos que recebe como parâmetro uma lista 
com números inteiros, verifica se tal lista possui elementos repetidos e os remove. 
A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. 
A lista devolvida deve estar ordenada.
Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
'''


def remove_repetidos(lista):
    for n in lista:
        if n not in lista2:
            lista2.append(n)
    print(sorted(lista2))

lista = [2, 4, 2, 2, 3, 3, 1]
lista2 = []

remove_repetidos(lista)