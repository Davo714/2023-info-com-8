# 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
# e imprima su índice de masa corporal (IMC).
# La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

pesoAltura = input("Ingrese su peso y su altura: ")
peso, altura = map(float, pesoAltura.split(","))
IMC = peso / (altura ** 2)
print(f"Su Indice de Masa Corporal (IMC) es de: {IMC}")