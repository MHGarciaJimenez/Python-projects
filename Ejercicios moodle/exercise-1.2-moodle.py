# Ejercicio 2: Programa que imprima si el número ingresado esta en el rango de 1 a 7

try:
    variable = int(input("Digite un numero: "))
except ValueError:
    print("Dato invalido")

if 1 <= variable <= 7:
    print("El numero está dentro del rango")
else:
    print("El numero está fuera del rango")