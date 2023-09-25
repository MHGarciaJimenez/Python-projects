#Calculador de promedio(media)

a = int (input("Ingrese el primer numero: "))
b = int (input("Ingrese el segundo numero: "))
c = int (input("Ingrese el tercer numero: "))

numeros = (a,b,c)

suma = a+b+c

valores = len(numeros)

promedio = suma/valores

print ("El promedio de los valores es: ", promedio)