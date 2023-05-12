# 4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
# pantalla si está aprobado (5 o más) o no.

nota = int(input("Ingrese la calificación: "))
if(nota >= 6 and nota <= 10):
    print("Está aprobado :)!")
elif(nota <= 5):
    print("Está desaprobado")
elif(nota > 10):
    print("La calificación ingresada no es válida.", end="\nEsta debe ir del 0 al 10.")
