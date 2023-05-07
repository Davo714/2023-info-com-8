# 15-Escribe un programa que solicite al usuario una temperatura en grados
# Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
# La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

temp = int(input("Ingrese la temperatura en °C: "))
C = temp
F = (C * 1.8) + 32

print(f"{temp} grados Celsius equivalen a {F} grados Fahrenheit")


