#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.Exiba o valor do desconto e o preço a pagar

produto = int(input('Qual é o valor da mercadoria?:R$ '))
percentual = int(input('Qual é o percentual de desconto?:% '))

porcentagem_soma = produto * percentual /100
calculo = produto - porcentagem_soma

print(f'Com desconto de R${porcentagem_soma:.2f} o valor passará para R${calculo:.2f}')