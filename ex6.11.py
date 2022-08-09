#Modifique o Programa 6.6 usando for. Explique por que nem todos os while podem ser transformados em for.

l = []
while True:
    n = n = int(input('Digite um número (0 sai): '))
    if n == 0:
        break
    l.append(n)
for v in l:
    print(l[v])