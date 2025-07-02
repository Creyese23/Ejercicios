#Hacer un algoritmo que lea 5 números y determine la suma entre ellos.
while True:
    # Solicitar al usuario que ingrese 5 números
    suma = 0
    n = input("Ingreso los N número: ")
    try:
        n = int(n)

        for i in range(n):
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numero = int(numero)
            suma += numero

            # Imprimir la suma de los 5 números ingresados
            print(f"La suma de los {n} números ingresados es: {suma}")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número válido.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saliendo del programa.")
        break