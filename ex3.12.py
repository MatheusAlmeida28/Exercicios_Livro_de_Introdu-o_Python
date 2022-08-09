#Escreva um programa que calcule o tempo de uma viagem de carro.Pergunte a distâcia a percorrer e a velocidade média esperada da viagem

distancia = int(input('Qual é a distância do destino?(km): '))
conversor = distancia*1000

carro_velocidade = 60

vel_med = distancia/carro_velocidade

print(f'Sua velocidade média será de {vel_med:.2f}m/s')
