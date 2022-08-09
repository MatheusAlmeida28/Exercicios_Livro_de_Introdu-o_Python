#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,assim como a quantidade de dias pelos quais o carro foi alugado.Calcule o preço a pagar que o carro custa R$ 60 por dia e R$0,15 por km rodado

carro_distancia = int(input('Qual foi distância percorrida?(Km): '))
carro_dias = int(input('Dias alugado(s): '))

calculo = (carro_dias * 60) + (carro_distancia*0.15)

print(f'O total pago será de R${calculo:.2f}')
