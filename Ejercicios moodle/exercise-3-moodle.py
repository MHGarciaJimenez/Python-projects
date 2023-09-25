#Ejercicio 3: Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
#             A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
import random

nombre = input("Escriba el nombre del alumno: ")

notas = []

suma = 0

for i in range(5):
    while True:
     calificación = float(input(f"Escriba la {i + 1}ra calificación a continuación: "))
     if 0<= calificación <= 10:
        break
     else:
        print("Calificación incorrecta, vuelva a intentarlo.")

    notas.append(calificación)

suma = sum(notas)
promedio = suma / len(notas)

maxima = max(notas)

minima = min(notas)

print("-------------------------------------------------")

print (f"El alumno {nombre} tiene las siguientes calificaciónes: {notas}")

print (f"La nota mas alta que obtuvo el alumno es: {maxima}")

print (f"La nota mas baja que obtuvo el alumno es: {minima}")

print (f"El promedio de las calificaciones del alumno {nombre} es {promedio}")