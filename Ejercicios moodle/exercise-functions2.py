#Ejercicio 2: Mostrar en pantalla los N primero número primos. 
#             Se pide por teclado la cantidad de números primos que queremos mostrar.

primos = []

def numero_primo (n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        cantidad = int(input("La cantidad de numeros primos que desea: "))
    except ValueError:
        print("Valor incorrecto")
        continue

    if cantidad <= 0:
        print("El numero debe ser positivo.")
        continue
    else:
        break

numero = 2

while len(primos) < cantidad:
    if numero_primo(numero):
        primos.append(numero)
    numero += 1

print(f"Los {cantidad} primeros numeros son: {primos}")