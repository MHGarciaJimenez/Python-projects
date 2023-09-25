# Ejercicio 4: Crea una aplicación que pida un número y calcule su factorial 
#              (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y 
#               se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).

while True:
    try:
        numero = int(input("Escriba el numero deseado: "))
    except ValueError:
        print("Valor incorrecto, intentelo de nuevo.")
        continue

    numeros_anteriores = [numero]
    multiplicacion = 1
    while numero>1:
        numero -= 1
        numeros_anteriores.insert(0,numero)
    for i in numeros_anteriores:
        multiplicacion *= i
    print(f"Resultado: {multiplicacion}")
        