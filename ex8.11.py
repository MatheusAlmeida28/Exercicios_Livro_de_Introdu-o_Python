'''Escreva uma função para validar uma variável string. Essa função
recebe como parâmetro a string, o número mínimo e máximo de caracteres.
Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e
mínimo, e falso, caso contrário.'''

def validar_string(string,minimo,maximo):
    total = 0
    for v in string:
        v
        total += 1
    if total < minimo or total > maximo:
        print('Erro, o valor foi maior que máximo ou menor que o minimo')
    else:
        print(f'Com o nome {string},o resultado deu {total} letras e foi maior que minimo {minimo} letras e menor que o máximo {maximo} letras')

nome = input('Qual nome deseja colocar: ').strip()
numero_min = int(input('Qual o minimo de letras que essa palavra pode ter?: '))
numero_max =int(input('Qual o máximo de letras que essa palavra pode ter?: '))

validar_string(nome,numero_min,numero_max)



