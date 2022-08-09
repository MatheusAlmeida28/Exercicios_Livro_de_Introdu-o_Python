#Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

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
terceira = primeira[:] 
terceira.extend(segunda)
x = 0
while x < len(terceira):
    print(f"índice {x}: valor: {terceira[x]}")
    x = x + 1