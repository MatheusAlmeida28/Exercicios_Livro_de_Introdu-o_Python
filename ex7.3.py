'''Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
1ª string: CTA
2ª string: ABC
3ª string: BT
A ordem dos caracteres da terceira string não é importante.'''

primeira = input("Digite a primeira string: ").upper()
segunda = input("Digite a segunda string: ").upper()

terceira = ""


for letra in primeira:
    if letra not in segunda and letra not in terceira:
        letra = letra + '-' #Adicionado um seta para separa as palavras
        terceira += letra

for letra in segunda:
    if letra not in primeira and letra not in terceira:
        letra = letra + '-' #Adicionado um seta para separa as palavras
        terceira += letra
    
if terceira == "":
    print("Caracteres comuns não encontrados.")
else:
    print(f"Caracteres diferentes: {terceira}")