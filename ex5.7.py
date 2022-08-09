#Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

tab = int(input('Tabuada de: '))
x = int(input('Digite o número inicial da tabuada: '))
y = int(input('Digite o número final da tabuada: '))
while x <= y:
    print(f'{tab} x {x} = {tab * x}')
    x = x + 1
