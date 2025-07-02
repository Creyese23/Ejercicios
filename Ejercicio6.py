#Codigo para imprimir por pantalla la categoria del alumno
while True:
    #Se solicita el promedio de las notas del alumno
    promedio = input("Ingrese el promedio de las notas del alumno: ")

    try:
        promedio = int(promedio)
        # Se determina la categoria del alumno basado en el promedio
        if promedio >= 0 and promedio <= 29:
            print("pesimo")
        elif promedio >= 30 and promedio <= 49:
            print("malo")
        elif promedio >= 50 and promedio <= 79:
            print("regular")
        elif promedio >= 80 and promedio <= 89:
            print("bueno")
        elif promedio >= 90 and promedio <= 100:
            print("excelente")
        else:
            print("Promedio no valido. Debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
        continue
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saliendo del programa.")
        break