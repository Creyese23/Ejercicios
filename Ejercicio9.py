#Obtener la suma de los primeros N números positivos.
while True:
    # Solicitar al usuario el valor de N
    n = input("Ingrese un número positivo N: ")
    try:
        n = int(n)
    # Validar que N sea positivo
        if n > 0:
            suma = 0
            for i in range(1, n + 1):
                suma += i
            print(f"La suma de los primeros {n} números positivos es: {suma}")
        else:
            print("Por favor, ingrese un número positivo mayor que 0.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero positivo.")
        continue
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saliendo del programa.")
        break
