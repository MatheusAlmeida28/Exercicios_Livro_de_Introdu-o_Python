'''Escreva uma função que retorne o maior de dois números.
Valores esperados:
máximo(5, 6) == 6
máximo(2, 1) == 2
máximo(7, 7) == 7
'''

def máximo(a, b):
    if a > b:
        return a
    else:
        return b


print(f"máximo(5,6) == 6 -> obtido: {máximo(5,6)}")
print(f"máximo(2,1) == 2 -> obtido: {máximo(2,1)}")
print(f"máximo(7,7) == 7 -> obtido: {máximo(7,7)}")
