#Escreva uma expresão que será ultilizada para decidir se um aluno foi ou não reprovado.Para ser aprovado
#todas as médias do aluno devem ser maiores que 7.Considere que o aluno cursa apenas três matérias,e que a nota
#de cada uma está armazenda nas seguintes variáveis: materia1,materia2 e materia3

print('Progrma simples que serve para descobrir se o aluno passou na média')

print('-'*50)

materia1 = float(input('Qual é valor de sua primeira matéria?: '))
materia2 = float(input('Qual é valor de sua segunda matéria?: '))
materia3 = float(input('Qual é valor de sua terceira matéria?: '))

media = (materia1+materia2+materia3)/3

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

