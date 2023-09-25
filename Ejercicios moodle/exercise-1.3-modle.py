# Ejercicio 3: Programa que calcule el interés de una cantidad si es mayor al 30%, sino informa el importe total.

try:
    valor_1 = float(input("Escriba la cantidad"))
except ValueError:
    print("Dato incorrecto.")

if valor_1 > 0.3:
    taza_interes = 0.05
    interes = valor_1 * taza_interes
    total = valor_1 + interes
    print(f"El interes es {interes}")
else:
    print("El importe total es {cantidad}")