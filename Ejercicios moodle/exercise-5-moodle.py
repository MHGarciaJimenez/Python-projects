import random
#Ejercicio 5: Crea una tupla con los meses del año, pide números al usuario, 
#             si el número está entre 1 y la longitud máxima de la tupla, 
#             muestra el contenido de esa posición sino muestra un mensaje de error. 
#             El programa termina cuando el usuario introduce un cero.

meses = [("Enero"),("Febrero"),("Marzo"),("Abril"),("Mayo"),("Junio"),("Julio"),("Agosto"),("Septiembre"),("Octubre"),("Noviembre"),("Diciembre")]

while True:
    try:
        numero = int (input("Escribe un numero del 1 al 12: "))
    except ValueError:
        print ("Dato incorrecto")
        continue

    mes= []

    if 1<= numero <=12:
        nueva_posicion = meses [numero-1]
        mes.append(nueva_posicion)
        print(mes)
        break