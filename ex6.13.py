#A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.

t = [ -10, -8, 0, 1, 2, 5, -2, -4]
minimo = t[0]
maximo = t[0]
soma = 0

for v in t:
    if v > maximo:
        maximo = v
    if v < minimo:
        minimo = v
    soma = soma + v

print(f'O valor máximo: {maximo}')
print(f'O valor mínimo:{minimo}')
print(f"Temperatura média: {soma / len(t)} °C")