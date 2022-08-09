#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

deposito = int(input('Qual é o valor de seu deposito inicial?: '))
juros = int(input('Qual é a quantidade de juros por mês?: '))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (juros / 100))
    print(f"Saldo do mês {mes} é de R${saldo:5.2f}.")
    mes = mes + 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito:8.2f}.")