# 11-Escribir un programa que pida al usuario dos números y muestre por pantalla
# la suma de ellos solo si ambos son pares.

numero = input("ingrese dos números: ")
num1, num2 = map(int, numero.split(","))
if(num1 % 2 == 0 and num2 % 2 == 0):
    print(f"La suma de ambos números es: {num1 + num2}")
elif(num1 % 2 != 0 and num2 % 2 == 0):
    print(f"El número {num1} no es par")
elif(num1 % 2 == 0 and num2 % 2 != 0):
    print(f"El número {num2} no es par")
else: print("Los números no son pares")
