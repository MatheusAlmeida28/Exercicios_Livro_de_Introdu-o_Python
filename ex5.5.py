#Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

fim = int(input('Digite o último número a imprimir: '))
x = 1
while x <= fim:
    if x % 3 == 0:
        print(x)
    x = x + 1


#Ou

'''
fim = 30
x = 3
while x <= fim:
    print(x)
    x = x + 3
'''