#Escreva um programa que converta um temperatura digitada em C em F.A fórmula para esse conversão é:

c = float(input("Digite a temperatura em °C:"))
f = (9 * c / 5) + 32
print(f"{c:.2f}°C é igual a {f:.2f}°F")