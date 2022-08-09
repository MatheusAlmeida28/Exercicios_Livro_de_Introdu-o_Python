#Altere o Programa 8.20 de forma que o usuário tenha três chances de acertar o número. O programa termina se o usuário acertar ou errar três vezes.

import random

n = random.randint(1, 10)
cont = 0

for contagem in range(3):
    x = int(input("Escolha um número entre 1 e 10:"))
    if x == n:
        print(f"Você acertou! digitando o número '{x}'")
        break
    else:
        print("Você errou.")
        cont += 1
print (f"O contador foi até {cont} tentaviva(s)")
