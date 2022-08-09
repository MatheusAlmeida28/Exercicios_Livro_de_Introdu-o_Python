#Modifique o programa do Exercício 6.9 de forma a pesquisar p e v em toda a lista e informando o usuário a posição onde p e a posição onde v foram encontrados.

#Meio que acabei fazendo no ex anteiror hahaha,Vou soemnte repetir

lista = [20, 25, 30, 35]
p = int(input("Digite o valor a procurar:"))
v = int(input("Digite o valor a procurar:"))
cont = 0
cont2 = 0
while cont < len(lista):
    if lista[cont] == p:
        break
    cont += 1
while cont2 < len(lista):
    if lista[cont2] == v:
        break
    cont2 += 1
if cont > cont2:
    primeiro = v 
if cont2 > cont:
    primeiro = p
else:
    primeiro = 'o mesmo'

print(f"{p} achado na posição {cont} e {v} foi achado na posição {cont2} e portanto o valor achado primeiro foi {primeiro}")
