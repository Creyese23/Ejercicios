#Codigo para imprimir por pantalla un numero del 0 al 9 en letras
while True:
    #Menu de opciones
    print("----------")
    print("|Menu: |")
    print("|0. Cero|")
    print("|1. Uno|")
    print("|2. Dos|")
    print("|3. Tres|")
    print("|4. Cuatro|")
    print("|5. Cinco|")
    print("|6. Seis|")
    print("|7. Siete|")
    print("|8. Ocho|")
    print("|9. Nueve|")
    print("----------")
    #Se solicita al usuario que ingrese un numero del 0 al 9
    num = input("Introduce un número del 0 al 9: ")
    try:
        num = int(num)
        # Condicionales para determinar el numero en letras
        if num == 0:
            print("Cero")
        elif num == 1:
            print("Uno")
        elif num == 2:
            print("Dos")
        elif num == 3:
            print("Tres")
        elif num == 4:
            print("Cuatro")
        elif num == 5:
            print("Cinco")
        elif num == 6:
            print("Seis")
        elif num == 7:
            print("Siete")
        elif num == 8:
            print("Ocho")
        elif num == 9:
            print("Nueve")
        else:
            print("Número no válido. Por favor, introduce un número del 0 al 9.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saliendo del programa.")
        break
# Fin del programa
# Este código imprime un menú de opciones para que el usuario elija un número del 0 al 9 en letras.
# Utiliza un bucle while para permitir múltiples intentos y maneja excepciones para entradas