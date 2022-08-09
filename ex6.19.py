'''Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
• os valores comuns às duas listas
• os valores que só existem na primeira
• os valores que existem apenas na segunda
• uma lista com os elementos não repetidos das duas listas.
• a primeira lista sem os elementos repetidos na segunda'''

L1 = [1, 2, 6, 8]
L2 = [3, 6, 8, 9]

print(f"Lista 1: {L1}")
print(f"Lista 2: {L2}")

conjunto_1 = set(L1)
conjunto_2 = set(L2)

print("Valores comuns às duas listas:", conjunto_1 & conjunto_2)
print("Valores que só existem na primeira:", conjunto_1 - conjunto_2)
print("Valores que só existem na segunda:", conjunto_2 - conjunto_1)

print("Elementos não repetidos nas duas listas:", conjunto_1 ^ conjunto_2)

print("Primeira lista, sem os elementos repetidos na segunda:",
      conjunto_1 - conjunto_2)