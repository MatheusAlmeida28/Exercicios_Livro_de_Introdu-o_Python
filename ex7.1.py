'''Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
1ª string: AABBEFAATT
2ª string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT'''

#Não tava correto mas gostei do código hahahah, é o sono hahahaha

string_1 = 'AABBEFAATT'
string_2 = 'BE'

while True:
    escolha = int(input('Em qual string deseja procurar [1] ou [2]?: '))
    if escolha == 1:
        nome = string_1
        letra = input('Qual letra que deseja encontrar?:  ').upper()
        if letra in string_1:
            rel = string_1.find(letra)
            break
        else:
            print('Não foi encontrado')
    elif escolha == 2:
        nome = string_2
        letra = input('Qual letra que deseja encontrar?:  ').upper()
        if letra in string_2:
            rel = string_2.find(letra)
            break
        else:
            print('Não foi econtrado')
    else:
        print('Erro,repita o processo')

print(f'Resultado: {letra} encontrado na posição {rel} de {nome}')

#O correto seria isso
'''
string_1 = input("Digite a primeira string: ")
string_2 = input("Digite a segunda string: ")

posicao = string_1.find(string_2)

if posição == -1:
    print(f"'{string_2}' não encontrada em '{string_1}'")
else:
    print(f"{string_2} encontrada na posição {posicao} de {string_1}")
'''
