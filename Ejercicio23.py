#Hacer un pseudocódigo que imprima los números impares hasta el 100 y que
#imprima cuantos impares hay.

nume = 0
cont = 0
while True:
    num = input("Ingrese un número: ")
    try:
        num = int(num)
        while nume <= num:
            if nume % 2 == 0:
                #print(f"{nume} es par")
                nume += 1
            else:
                print(f"{nume} es impar")
                # Incrementar el contador de números impares
                cont += 1
                nume += 1
        
        print(f"Total de números impares hasta {num}: {cont}")

            
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