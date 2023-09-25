import random

#Ejercicio 1: Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
#             y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

for i in range(10):
    i = random.randint(1,10)
    print("El valor de la lista es: ",i)
    print("El cuadrado de ", i," es: ", i**2)
    print(i, "elevado al cubo es: ", i**3)
    print("--------------------------------------------")