# 3-Escribir un programa que pida al usuario dos números y muestre por pantalla
# cuál de ellos es mayor.

numeros = input("Ingrese dos números: ")
num1, num2 = map(int, numeros.split(","))

if(num1 < num2):
    print(f"Entre ambos números {num2} es el mayor")
else: print(f"Entre ambos números {num1} es el mayor")