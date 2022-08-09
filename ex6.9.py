#Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado. Na impressão, indique qual dos dois valores foi achado primeiro.

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
