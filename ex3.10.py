#Faça um progrma que calcule o aumento de um salário.Ele deve solicitar o valor do salário e a procentagem do aumento.Exiba o valor do aumento e do novo usuário

salario = int(input('Digite seu salário:R$ '))
aumento = int(input('Digite seu aumento %: '))

calculo = salario + (salario*aumento/100)

print(f'Seu salário novo será de R${calculo:.2f}')