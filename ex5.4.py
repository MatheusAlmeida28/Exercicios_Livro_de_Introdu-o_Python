#Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

fim = int(input('Digite o último número a imprimir: '))
x = 1
while x <= fim:
    if not x % 2 == 0:
        print(x)
    x = x + 1

#Ou

'''
fim = int(input("Digite o último número a imprimir:"))
x = 1
while x <= fim:
    print(x)
    x = x + 2
'''