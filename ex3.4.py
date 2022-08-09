#Escreve um expressão para determinar se uma pessa deve ou não pagar imposto. Considere que
# pagam imposto pessoas cujo o salário é maior que R$ 1200,00

print('Vamos descobrir se você pagará imposto com base no seu salário')

print('-'*40)

pessoa_salario = float(input('Digite o valor de seu salário:R$ '))

print('-'*40)

if pessoa_salario > 1200:
    print(f'Você pagará imposto nesse caso')
else:
    print(f'Você não pagará imposto nesse caso')
