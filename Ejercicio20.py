#Realice un seudocódigo que represente el algoritmo para obtener el área de un triangulo.

while True:
    # Solicitar al usuario la base y la altura del triángulo
    area = 0.0
    base = input("Ingrese la base del triángulo: ")
    altura = input("Ingrese la altura del triángulo: ")
    try:
        base = float(base)
        altura = float(altura)
        # Validar que la base y la altura sean positivas
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area:.2f}")
    except ValueError:
        print("Por favor, introduce un número válido.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar != 's':
        print("Entrada no válida. Por favor, ingrese 's' para continuar o 'n' para salir.")
        break
 