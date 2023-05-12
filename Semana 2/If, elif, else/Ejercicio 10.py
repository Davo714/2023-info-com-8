# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante.

letra = input("Ingrese una letra: ")
if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print(f"{letra} es una vocal")  
elif(letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):
    print(f"{letra} es una vocal")
else: print(f"{letra} es una consonante")
