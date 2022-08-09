#Escreva um programa que leia três números e que imprima o maior e o menor.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

maior = num2

if num1 > num2 and num1 > num3:
    maior = num1
if num3 > num2:
    maior = num3

menor = num2

if num1 < num2 and num1 < num3:
    menor = num1
if num3 < num2:
    menor = num3
    
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")