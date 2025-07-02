#Pinturas “Pintuco” requiere determinar cuánto cobrar por trabajos de pinturas.
#Considere que se cobra m2 y realice un seudocódigo que represente el algoritmo
#que le permita ir generando la cotización para cada cliente.

# Pinturas "Pintuco" requiere determinar cuánto cobrar por trabajos de pinturas.
# Considere que se cobra por metro cuadrado (m2) y realice un seudocódigo que represente el algoritmo
# que le permita ir generando la cotización para cada cliente.
while True:
    # Definir el precio por metro cuadrado
    precio_por_m2 = input("Ingrese el precio por metro cuadrado: ")

    try:
        precio_por_m2 = float(precio_por_m2)
        # Solicitar al usuario las dimensiones del área a pintar
        ancho = input("Ingrese el ancho del área a pintar (en metros): ")
        largo = input("Ingrese el largo del área a pintar (en metros): ")
        try:
            ancho = float(ancho)
            largo = float(largo)
            # Calcular el área en metros cuadrados
            area = ancho * largo

            # Calcular el costo total
            costo_total = area * precio_por_m2

            # Mostrar el resultado al usuario
            print(f"El área a pintar es: {area:.2f} m²")
            print(f"El costo total de la pintura es: ${costo_total:.2f}")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos para las dimensiones.")
    except ValueError:
        print("Por favor, ingrese un precio válido por metro cuadrado.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar != 's':
        print("Entrada no válida. Por favor, ingrese 's' para continuar o 'n' para salir.")
        break
# Fin del programa