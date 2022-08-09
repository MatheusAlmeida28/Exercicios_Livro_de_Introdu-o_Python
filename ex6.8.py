#Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída do while.

lista = [20, 25, 30, 35]
p = int(input("Digite o valor a procurar:"))
cont = 0
while cont < len(lista):
    if lista[cont] == p:
        break
    cont += 1
print(len(lista))
if cont < len(lista):
    print(f"{p} achado na posição {cont}")
else:
    print(f"{p} não encontrado")