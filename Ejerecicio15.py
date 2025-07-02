#Introducir dos números por teclado y mediante un menú, calcule su suma, su
# resta, su multiplicación o su división.

operacion = ""
resultado = 0

while True:
    # Solicitar al usuario que introduzca dos números
    print("Introduce dos números:")
    num1 = input("Número 1: ")
    num2 = input("Número 2: ")

    try:
        num1 = float(num1)
        num2 = float(num2)

        print("\nMenú de operaciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Modulo")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            resultado = num1 + num2
            operacion = "Suma"
        elif opcion == '2':
            resultado = num1 - num2
            operacion = "Resta"
        elif opcion == '3':
            resultado = num1 * num2
            operacion = "Multiplicación"
        elif opcion == '4':
            if num2 != 0:
                resultado = num1 / num2
                operacion = "División"
            else:
                print("Error: División por cero.")
        elif opcion == '5':
            if num2 != 0:
                resultado = num1 % num2
                operacion = "Modulo"
            else:
                print("Error: División por cero.")
        else:
            print("Opción no válida.")
            # Imprimir el resultado de la operación
        print(f"Resultado de la {operacion}: {resultado}")
    except ValueError:
        print("Por favor, introduce números válidos.")

    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas realizar otra operación? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar != 's':
        print("Entrada no válida. Por favor, ingrese 's' para continuar o 'n' para salir.")
        break