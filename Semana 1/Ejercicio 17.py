# 17-Escribe un programa que solicite al usuario dos palabras y luego las imprima
# en orden inverso.
# Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
# "mundo hola".
# Importante!!! Utiliza un solo print() 😈.

palabras = input("Ingrese 2 palabras de su preferencia: ")
pal1, pal2 = map(str, palabras.split(","))

print(pal2 + " " + pal1)