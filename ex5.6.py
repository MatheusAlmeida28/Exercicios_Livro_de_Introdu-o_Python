#Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4, …

tab = int(input('Tabuada de: '))
x = 1
while x <= 10:
    print(f'{tab} x {x} = {tab * x}')
    x = x + 1