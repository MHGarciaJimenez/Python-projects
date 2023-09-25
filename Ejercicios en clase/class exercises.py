#Ejercicio 1

#lista = (13,20,17,14,8,25)
#suma = sum (lista)
#datos = len (lista)
#promedio = suma/datos

#if promedio == 30:
    #print("El promedio es el esperado: ", promedio)
#elif promedio < 30:
    #print ("El promeidio es menor al esperado")
#else:
    #print ("El promedio es superior a lo esperado")
#print ("Promedio esperado: 30")
#print ("El promedio obtenido es: ", promedio)

#-------------------------------------------------------------------------------------------------------------
#Ejercicio 2

#edad = int ( input ("Ingresar el año de nacimiento: "))

#if edad<=2005:
    #print ("Ya eres mayor de edad")
#else:
    #print ("Aún eres menor de edad")

#--------------------------------------------------------------------------------------------------------------
#Ejercicio 3

#puntos = int (input ("Cual es el puntaje que obtuvo en el examen? "))

#if puntos<=5:
    #print ("Tienes una calificación reprobatoria")
#elif puntos == 6:
    #print ("Tu calificación es 6.")
#elif puntos == 7:
    #print ("Tu calificación es 7")
#elif puntos == 8:
    #print ("Tu calificación es 8")
#elif puntos == 9:
    #print ("Felicidades, acreditaste con 9")
#else:
    #print("Felicidades, exentaste con 10")

#-------S I G U I E N T E - C L A S E: B U C L E S ----------------------------------------------------------
#Ejercicio 1
import random

#lista = []
#pares =[]
#resultado = []

#for _ in range(20):
    #numero = random.randint(1,100)
    #lista.append(numero)
    #if numero % 2 == 0:
        #pares.append(numero)
    #resultado = sum (pares)

#print(lista)
#print(pares)
#print(resultado)

#----------------------------------------------------------------------------------------------
#Ejercicio 2
#contador = 10

#while contador >= 1:
    #print(contador)
    #contador -= 1

#----------------------------------------------------------------------------------------------
#Ejercicio 3
#multiplicando = int (input("Escribe el numero que deseas: "))

#for contador in range(1,11):
    #resultado = multiplicando*contador
    #print (multiplicando, "+" ,contador, "=",resultado)
     
#----------------------------------------------------------------------------------------------
#Ejercicio 4
#suma = 0

#contador = 0

#while True:
    #edad = input("Ingresa la edad del alumno (o escribe -fin- para terminar): ")
    #if edad.lower() == "fin":
        #break
    #try:
        #edad = int(edad)
    #except ValueError:
        #print("Ingresa una edad valida o -fin- para terminar.")
        #continue
    #suma += edad
    #contador += 1

#if contador>0:
    #promedio = suma/contador
    #print(f"El promedio de edades de {contador} alumnos es : {promedio:.2f}")
#else:
    #print("No se ingresaron edades validas.")

#-------------------------------------------------------------------------------------------------
#Ejercicio 4.2

#cadena = input("Digite las edades de los alumnos separadas por una coma: ")

#lista = cadena.split(",")

#lista_numeros = [int(cadena) for cadena in lista]

#suma = 0

#for i in lista_numeros:
    #suma += i

#promedio = suma/len(lista_numeros)

#print("La edad promedio de los", len(lista_numeros), "alumnos, es: ", promedio)