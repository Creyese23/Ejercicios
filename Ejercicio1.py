#Codigo que me imrime por pantalla la estacion del año
while True:
    #Menu de opciones
    print("----------")
    print("|Menu: |")
    print("|1. Invierno|")
    print("|2. Primavera|")
    print("|3. Verano|")
    print("|4. Otoño|")
    print("----------")

    # Solicitar al usuario que ingrese un numero del 1 al 4
    num = input("Introduce un número del 1 al 4: ")
    try:
        num = int(num)
        # Condicionales para determinar la estación del año
        if num == 1:
            print("Invierno")
            break
        elif num == 2:
            print("Primavera")
            break
        elif num == 3:
            print("Verano")
            break
        elif num == 4:
            print("Otoño")
            break
        else:
            print("Número no válido. Por favor, introduce un número del 1 al 4.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saliendo del programa.")
        break