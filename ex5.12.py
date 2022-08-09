#Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

deposito = int(input('Qual é o valor de seu deposito inicial?: '))
juros = int(input('Qual é a quantidade de juros por mês?: '))
investimento = float(input("Depósito mensal: "))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (juros / 100)) + investimento
    print(f"Saldo do mês {mes} é de R${saldo:5.2f}.")
    mes += 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito:8.2f}.")