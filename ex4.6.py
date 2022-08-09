#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

km = int(input('Qual é a quantidade de km(s) que você deseja andar?: '))
if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45

print(f'Você pagará R${valor:.2f} pela corrida em Km(s)')