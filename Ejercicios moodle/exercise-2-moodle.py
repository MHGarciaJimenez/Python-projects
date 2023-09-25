#Ejercicio 2: Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado.
#             Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

oracion = input("Escriba una oración ---> ")

lista = oracion.split(" ")

print(lista)

reverso = lista[::-1]

print(reverso)
