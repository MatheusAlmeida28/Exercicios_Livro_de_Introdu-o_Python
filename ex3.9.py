#Escreva um programa que leia a quantidade de dias,horas,minutos e segundos do usuário.Calcule o total em segundos

print('Convsersor do tempo para segundos')
print('-'*50)

hora = int(input('Qual é(são) a quantidade(s) de hora(s)?: '))
segundos_hora = hora * 3600 

minutos = int(input('Qual é(são) a quantidade(s) de minuto(s)?: '))
segundos_minuto = minutos * 60

segundos = int(input('Qual é(são) a quantidade(s) de segundos(s)?: '))

print(f'O total de segundos será de {segundos_hora + segundos_minuto + segundos}s')