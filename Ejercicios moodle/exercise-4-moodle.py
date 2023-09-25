import random
#Ejercicio 4: Codifica un programa en Python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. 
#             Cada alumno puede tener distinta cantidad de notas. 
#             Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listados con las notas de cada alumno. 
#             El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.
#             Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
#             Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

salon_de_clase = {}
lista_de_tuplas = []

while True:
    try:
        cantidad = int(input("Escribe la cantidad de alumnos que se van a registrar: "))
    except ValueError:
        print("Dato invaido, vuelva a repetirlo")
        continue
    nombres = input("Escriba el/los nombres, separados por una coma: ")
    lista_nombres = nombres.split(",")

    if len(lista_nombres) != cantidad:
        print(f"El registro solo almacenará {cantidad} alumnos, vuelva a intentarlo")
        continue

    se_repite = False

    for i in lista_nombres:
        if lista_nombres.count(i) > 1:
            se_repite = True
            print(f"El nombre {i} no se puede repetir, vuelva a intentarlo.")
            continue


    for nombre in lista_nombres:
        str_calificaciones = input(f"Escriba las calificaciones del alumno {nombre} separadas con una coma: ")
        notas_lista = str_calificaciones.split(",")
        lista_a_num = [float(calificaciones) for calificaciones in notas_lista]
        promedio = sum(lista_a_num)/len(lista_a_num)
        lista_de_tuplas.append((nombre,promedio))
        salon_de_clase[nombre] = lista_a_num
    print("Registro completo")
    break
print("------------------------------------------------------------------------")

print(f"La información registrada es: ")
for nombre,calificaciones in salon_de_clase.items():
    print(f"nombre: {nombre},",f"calificaciones {calificaciones}")

print("------------------------------------------------------------------------")

print("Esta es la lista de alumnos y su promedio")
for i in lista_de_tuplas:
    print(i)

