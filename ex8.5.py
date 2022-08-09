#Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesquisa em lista, vistos no Capítulo 7.

def pesquisa(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None


L = [10, 20, 25, 30]
print(pesquisa(L, 25))
print(pesquisa(L, 27))