# 5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más
# grande en el conjunto.

numeros = {1,2,3,4,5,6,7,8,9,10}
max=0
for numero in numeros:
    if max < numero:
        max = numero
print(f"El valor más grande del conjunto es {max}")