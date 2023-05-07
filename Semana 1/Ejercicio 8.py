# 8-Crea un programa que pida al usuario el radio de un círculo y muestre su
# diámetro, su circunferencia y su área.
# Supón que pi es aproximadamente 3.14159

radio = float(input("Ingrese el radio del circulo: "))
pi = 3.14159
A = pi * radio*radio
D = radio * 2
C = pi * D
print(f"El diámetro del círculo es: {D}, su cincurferencia: {C}, y el área: {A}")