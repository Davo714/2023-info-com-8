# 18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de
# residencia, y lo muestre en pantalla Utilizando una sola línea de código.
# *Recuerda el print() del ejercicio anterior 

nombre = input("Hola, cuál es su nombre? ")
edad = int(input(f"{nombre}, qué edad tienes? "))
resid = input("En qué ciudad resides? ")

print(f"Entonces, te llamas {nombre}, tienes {edad} años y vives en {resid}.")