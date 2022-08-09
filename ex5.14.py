#Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

s = 0
cont = 0
while True:
    v = int(input('Digite um valor ou 0 para sair: ')) 
    if v == 0:
        break
    s+=v
    cont += 1
media = s/cont
print(f'A quantidade de números digitados {cont}, sua soma é de {s} e sua média é {media:.2f}')