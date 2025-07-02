#Escribir un programa que permita introducir por teclado tres letras y
# respondan si existen al menos dos letras iguales. 

while True:
    # Solicitar al usuario que ingrese tres letras
    letra1 = input("Ingrese la primera letra: ")
    letra2 = input("Ingrese la segunda letra: ")
    letra3 = input("Ingrese la tercera letra: ")
    try:
        letra1 = str(letra1)
        letra2 = str(letra2)
        letra3 = str(letra3)
        # Verificar si al menos dos letras son iguales
        if letra1 == letra2 or letra1 == letra3 or letra2 == letra3:
            print("Existen al menos dos letras iguales.")
        else:
            print("No existen letras iguales.")
    except ValueError:
        print("Por favor, ingrese letras válidas.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar == 's':
        continue