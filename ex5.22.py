#Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
#Imprima a tabuada da operação escolhida.
#Repita até que a opção saída seja escolhida.

while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 5:
        break
    elif escolha >= 1 and escolha < 5:
        n = int(input("Tabuada de: "))
        x = 1
        while x <= 10:
            if escolha == 1:
                print(f"{n} + {x} = {n + x}")
            elif escolha == 2:
                print(f"{n} - {x} = {n - x}")
            elif escolha == 3:
                print(f"{n} / {x} = {n / x:5.4f}")
            elif escolha == 4:
                print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        print("Opção inválida!")
print('Fim do programa')
