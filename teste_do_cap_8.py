'''def barra(a):
    print("*" * a)

barra(10)

def barra(n=40, caractere="*"):
    print(caractere * n)

barra(n=50,caractere="j")
barra(50,'p')

def soma(valor1,valor2,valor3 = 1):
    soma = valor1 + valor2 + valor3
    print(valor1)
    print(valor2)
    if valor3 > 0:
        print(valor3)
    print(soma)


soma(valor2 = 10,valor1 = 20)


def soma(a, b):
    return a + b


def subtração(a, b):
    return a - b


def imprime(a, b, chamada):
    print(chamada(a, b))


imprime(5, 4, soma)
imprime(10, 1, subtração)

def imprime_lista(L, fimpressão, fcondição):
    for e in L:
        if fcondição(e):
            fimpressão(e)


def imprime_elemento(e):
    print(f"Valor: {e}")


def épar(x):
    return x % 2 == 0


def éimpar(x):
    return not épar(x)


L = [1, 7, 9, 2, 11, 0]
imprime_lista(L, imprime_elemento, épar)
print('-'*50)
imprime_lista(L, imprime_elemento, éimpar)


# * = desempactar no caso abaixo ,soma(*L).

def soma(a,b,c='*'):
    c = 0
    print(a + b + c )

L = [2,3]

soma(*L)

#Outro caso é desempacotar listas,exemplo abaixo. com * , não se esqueça

def barra(n=10, c="*"):
    print(c * n)

L = [[5, "-"],  [10, "*"],  [5], [6, "."]]

for e in L:
    barra(*e)

def soma(*args):
    s = 0
    for x in args:
        s += x
    print (s)


soma(1, 2)
soma(2)
soma(5, 6, 7, 8)
soma(9, 10, 20, 30, 40)

def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)


imprime_maior("Maior:", 5, 4, 3, 1, 15)
imprime_maior("Max:", *[1, 7, 9])
imprime_maior("Max:")


# funções lambda

a = lambda x: x * 2
print(a(3))

# Exceções

nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir:"))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
    except IndexError:
        print("Valor inválido, digite entre -3 e 2")


# Para caso dê erro mas vc não quer deixar o código quebrar
nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir:"))
        print(nomes[i])
    except Exception as erro:
        print(f"Algo de errado aconteceu: {erro}")

#finally

nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir:"))
        print(nomes[i])
    except ValueError as e:
        print("Digite um número!")
    finally:
        print(f"Tentativa {tentativa + 1}")


#raise

nomes = ["Ana", "Carlos", "Maria"]
try:
    i = int(input("Digite o índice que quer imprimir:"))
    print(nomes[i])
except ValueError as e:
    print("Digite um número!")
    raise
finally:
    print(f"Sempre o finally é executado")


#editar uma exceção com raise

def epar(n):
    try:
        print(n % 2)
    except Exception:
        raise ValueError("Valor inválido")

epar(2) #certo
epar("act") #errado'''

# o else é usado casi exista nenhuma exceção

while True:
    try:
        v = int(input("Digite um número inteiro (0 sai):"))
        if v == 0:
            break
    except Exception:
        print("Valor inválido! Redigite")
    else:
        print("Parabéns, nenhuma exceção")
    finally:
        print("Executado sempre, mesmo com break")







