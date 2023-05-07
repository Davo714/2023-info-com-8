# 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()

# txt = "welcome to the jungle"

# x = txt.split()

# print(x)

fechaNac = (input("Ingrese su fecha de nacimiento: dd/mm/aaaa: "))
dia, mes, anio = map(int, fechaNac.split("/"))

import datetime 
fechaAct = datetime.date.today()
diaAct = fechaAct.day
mesAct = fechaAct.month
anioAct = fechaAct.year

edad = anioAct - anio

if(mes > mesAct):
    edad = edad - 1
    print(f"Tienes actualmente {edad} años")
elif((mes == mesAct) and (dia == diaAct)):
    print(f"Feliz cumpleaños! {edad} no es nada :)")
elif((mes == mesAct) and (dia < diaAct)):
    print(f"Se acerca tu cumpleaños! ya se sienten esos {edad} años")
elif((mes == mesAct) and (dia <= diaAct+3)):
    print(f"Feliz cumpleaños N° {edad} atrasado!")