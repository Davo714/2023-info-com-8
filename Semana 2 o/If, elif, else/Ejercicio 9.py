# 9-Escribir un programa que pida al usuario tres números y muestre por pantalla
# el mayor de ellos.

numeros = (input("Ingrese 3 números: "))
num1, num2, num3 = map(int, numeros.split(","))
if(num1 > num2 and num1 > num3):
    print(f"{num1} es el número mayor")
elif(num2 > num1 and num2 > num3):
    print(f"{num2} es el número mayor")
else: print(f"{num3} es el número mayor")
