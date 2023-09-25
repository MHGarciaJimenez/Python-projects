# Ejercicio 1: Programa que imprima si el número es positivo o negativo.

try:
    variable = int(input("Digite un numero: "))
except ValueError:
    print("Dato invalido.")

if variable >= 0 :
    print("El numero es positivo.")
else:
    print("El numero es negativo.")