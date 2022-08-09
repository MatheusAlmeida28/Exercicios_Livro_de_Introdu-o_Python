#Modifique o programa 2.2,de forma que ele calcule um aumento de 15% para um salário de R$ 750

salario = 750
aumento = 15
soma = salario+(salario*aumento/100)
print(f'Com o aumento,o salário subirá de R$750,00 para R${soma:.2f}')
