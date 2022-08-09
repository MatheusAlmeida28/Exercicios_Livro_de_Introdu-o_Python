#Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

from itertools import count


primeira = []
segunda = []
while True:
    adicionar = int(input("Digite um valor para a primeira lista (0 para terminar): "))
    if adicionar == 0:
        break
    primeira.append(adicionar)
while True:
    adicionar = int(input("Digite um valor para a segunda lista (0 para terminar): "))
    if adicionar == 0:
        break
    segunda.append(adicionar)

terceira = []
duas_listas = primeira[:]
duas_listas.extend(segunda)

print(duas_listas)

for i in duas_listas:
    if i not in terceira:
        terceira.append(i)
        print

print(terceira)