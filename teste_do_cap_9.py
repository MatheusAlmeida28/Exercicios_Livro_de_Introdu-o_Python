'''#Criar um arquivo e escrver nele
# obs: Ele vai sobrescrver caso exista um texto anterior 

arquivo = open("números.html", "w")
for linha in range(1, 101):
    arquivo.write(f"{linha}\n")
arquivo.write('Terminei aqui')
arquivo.close()

#Abrindo, lendo e fechando um arquivo
arquivo = open("números.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#Uso do with  - mais indicado que usar o close
with open("números.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)

import sys
print(f"Número de parâmetros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")

# Programa 9.7 Criação de uma página inicial em HTML
with open("página.html", "w", encoding="utf-8") as página:
    página.write("<!DOCTYPE html>\n")
    página.write("<html lang=\"pt-BR\">\n")
    página.write("<head>\n")
    página.write("<meta charset=\"utf-8\">\n")
    página.write("<title>Título da Página</title>\n")
    página.write("</head>\n")
    página.write("<body>\n")
    página.write("Olá!")
    for l in range(10):
        página.write(f"<p>{l}</p>\n")
    página.write("</body>\n")
    página.write("</html>\n")'''

import os
os.getcwd()