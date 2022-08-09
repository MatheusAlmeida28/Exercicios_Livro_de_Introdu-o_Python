'''Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura) / 2).
Valores esperados:
área_triângulo(6, 9) == 27
área_triângulo(5, 8) == 20

Resposta:'''

def area_triangulo(a,b):
    area = a * b / 2
    return area

print(area_triangulo(6, 9))