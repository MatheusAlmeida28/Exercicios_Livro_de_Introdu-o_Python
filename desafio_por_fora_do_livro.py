# Desafio 1 - Exiba todos os nomes dos inscritos que estão no arquivo inscritos.txt no console

'''with open("inscritos.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)'''

# Desafio 2 - Adicione o seu nome na lista de inscritos e depois todos os nomes que estão no arquivo inscritos.txt no console

'''with open("inscritos.txt", "a") as arquivo:
    arquivo.write('\nMatheus Almeida')'''

# Desafio 3 - Com o seu nome já na lista de inscritos, exiba o nome de cada pessoas que está inscrito na lista + o número que ele representa na lista em ordem crescente (ex: 1 jhonatan , 2 Patricio Silva, 3 Kid Boy 3000)

'''with open("inscritos.txt", "r") as arquivo:
    cont = 1
    for linha in arquivo.readlines():
        print(f'{cont} - {linha}')
        cont += 1'''

# ou 

with open('inscritos.txt', 'r') as arquivo:
    for key, valores in enumerate(arquivo):
        print(key + 1, valores)