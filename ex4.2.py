#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidadade_usuario = int(input('Qual a sua velociadade em km/s?: '))

if velocidadade_usuario > 80:
    calculo = (velocidadade_usuario - 80) * 5
    print(f'Você terá que pagar a multa de R${calculo} ')
else:
    print('Você não pagara multa')