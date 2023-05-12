# 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
# por pantalla si contiene la letra "a".
    
caracteres = input("Ingrese la cadena de caracteres: ")
for i in range(len(caracteres)):
    if caracteres[i]== "a" or caracteres[i]== "A":
        print("Contiene la letra 'a'")
    else: print("No contiene la letra 'a'")
    break
#Se puede mejorar, solo entrega la letra 'a' si esta va primero. si ponemos más caracteres
#o una frase, no la reconoce

