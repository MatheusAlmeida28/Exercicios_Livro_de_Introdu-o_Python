#Altere o Programa 6.11 de forma a imprimir o menor elemento da lista.

L = [4, 2, 1, 7]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)