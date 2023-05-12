# 2-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es positivo, negativo o cero.

numero = int(input("Ingrese un número: "))
if(numero == 0):
    print("El número es cero.")
elif(numero < 0):
    print("El número es negativo.")
else: print("Es número es positivo.")