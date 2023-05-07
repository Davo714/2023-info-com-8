# 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
# imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

nombre = input("Hola, cuál es su nombre? ")
edad = int(input(f"{nombre}, que edad tienes? "))
print(f"{nombre} dentro de 10 años vas a tener {edad+10} años!")