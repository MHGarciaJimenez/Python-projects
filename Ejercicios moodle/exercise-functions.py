# Ejercicio 1: Realizar un ejemplo de menú, 
#              donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

while True:
    def opcion1 ():
        print("Elegiste la opcion 1")

    def opcion2 ():
        print("Elejiste la opción 2")

    def opcion3 ():
        print("Elejiste la opción 3")

    def menu ():
        print("Menú: ")
        print("1.-  Elige Opción 1")
        print("2.-  Elige Opción 2")
        print("3.-  Elige Opción 3")
        print("4.-  Salir")

    menu()

    decision = input("Elije el numero de la opción deseada: ")

    if decision == "1":
        opcion1()
    elif decision == "2":
        opcion2()
    elif decision == "3":
        opcion3()
    elif decision == "4":
        print("Saliste del menú")
        break
    else:
        print("Elección invalida.")
        continue

    print("-----------------------------------------------------------------")