#Codigo para imprimir la estacion del año dependiendo del mes
while True:
    # Menú de opciones
    print("----------")
    print("|Menu: |")
    print("|12, 1 o 2. Invierno|")
    print("|3, 4 o 5. Primavera|")
    print("|6, 7 o 8. Verano|")
    print("|9, 10 o 11. Otoño|")
    print("----------")
    # Solicitar al usuario que ingrese un número del 1 al 12
    mes = input("Introduce un número del 1 al 12: ")
    try:
        mes = int(mes)
        # Condicionales para determinar la estación del año
        if mes == 12 or mes == 1 or mes == 2:
            print("Invierno")
        elif mes == 3 or mes == 4 or mes == 5:
            print("Primavera")
        elif mes == 6 or mes == 7 or mes == 8:
            print("Verano")
        elif mes == 9 or mes == 10 or mes == 11:
            print("Otoño")
        else:
            print("Número no válido. Por favor, introduce un número del 1 al 12.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
        continue
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saliendo del programa.")
        break