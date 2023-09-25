# Ejercicio 3: Una persona adquirió un producto para pagar en 20 meses. 
#              El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
#              Realizar un algoritmo para determinar cuánto debe pagar mensualmente
#              y el total de lo que pagó después de los 20 meses.

def pago(cantidad):
    acumulado = [cantidad]
    print(f"La primer mensualidad es de: €{cantidad}")
    for i in range(19):
        i += 1
        mensualidad = cantidad * 2
        cantidad += cantidad
        acumulado.append(cantidad)
        print(f"{i}.- La siguiente mensualidad es de: €{mensualidad}")
        total = sum(acumulado)
    print(f"El total de su pago es: {total}")

historial = pago(10)

print(pago)