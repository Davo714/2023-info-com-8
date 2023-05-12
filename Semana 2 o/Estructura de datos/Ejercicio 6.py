# 6-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número
# de elementos en el conjunto.

numeros = {1,2,3,4,5,6,7,8,9,10}
numeros2 = set()
for numero in numeros:
    if numero % 2 == 1:
        numeros2.add(numero)
print(f"Los numeros impares del conjunto son: {numeros2}")
