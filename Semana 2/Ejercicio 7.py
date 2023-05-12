# 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
# es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter = input("ingrese un carácter: ")
if(caracter.isalpha()):
    if(caracter.islower()):
        print("Es una letra minúscula.")
    else: print("Es una letra mayúscula.")
elif(caracter.isdigit()):
    print("Es un número.")
else: print("Es un caracter especial.")
