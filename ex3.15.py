#Escreva um programa para calcular a redução do tempo de vida de um fumante.Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.Considere que um fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um fumante.Exiba o total de dias

cigarros_por_dia = int(input('Qual de media de cigarro(s) por dia?: '))
anos_usando_cigarro = int(input('Qual é a quantidade de ano(s) usando cigarro?: '))

calculo_minutos = anos_usando_cigarro * 365 * cigarros_por_dia * 10

dias_reduzidos = calculo_minutos / (24 * 60)
print(f'{dias_reduzidos:.2f} dias')
