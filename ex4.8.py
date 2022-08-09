#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada

num1 = int(input('Digite um numéro inteiro: '))
num2 = int(input('Digite um numéro inteiro: '))

escolha = int(input('O que deseja fazer com eles? [1]Soma [2]Subtração [3]Multiplicação [4]Divisão : '))

if escolha == 1:
    soma = num1 + num2
    print(f'A soma de {num1} e {num2} será de {soma}')

elif escolha == 2:
    subtracao = num1 - num2
    print(f'A subtração de {num1} e {num2} será de {subtracao}')

elif escolha == 3:
    multiplicacao = num1 * num2
    print(f'A multiplicação de {num1} e {num2} será de {multiplicacao}')

elif escolha == 4:
    divisao = num1 / num2
    print(f'A divisão de {num1} e {num2} será de {divisao}')

else:
    print('O comando digitado não existe')