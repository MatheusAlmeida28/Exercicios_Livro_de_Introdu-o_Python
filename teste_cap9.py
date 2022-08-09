arquivo = open("números.html", "w")
for linha in range(1, 102):
    arquivo.write(f"{linha}\n")
arquivo.write('Terminei aqui')
arquivo.close()