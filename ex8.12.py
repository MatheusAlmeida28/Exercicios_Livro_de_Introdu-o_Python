'''Escreva uma função que receba uma string e uma lista.
A função deve comparar a string passada com os elementos da lista, também passada como parâmetro.
Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.'''

def procurar_string(s, lista):
    return s in lista


L = ["AB",  "CD", "EF", "FG"]

print(procurar_string("AB", L))
print(procurar_string("CD", L))
print(procurar_string("EF", L))
print(procurar_string("FG", L))
print(procurar_string("XYZ", L))