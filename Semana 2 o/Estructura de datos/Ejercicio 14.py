# 14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los
# elementos de la tupla.
numeros = (1,2,3,4,5)
suma = 0
for num in numeros:
    suma += num
print(f"La suma de la tupla es: {suma}")