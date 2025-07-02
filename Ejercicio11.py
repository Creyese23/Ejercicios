#Algoritmo que solicita un número y genere su correspondiente tabla de multiplicar desde 1 hasta 10. 

while True:
    try:
        # Solicitar al usuario un número
        numero = int(input("Ingrese un número para generar su tabla de multiplicar (o '0' para salir): "))
        if numero == 0:
            print("Saliendo del programa.")
            break
        # Generar la tabla de multiplicar del número ingresado
        print(f"Tabla de multiplicar del {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar != 's':
        print("Entrada no válida. Por favor, ingrese 's' para continuar o 'n' para salir.")
        break
# Fin del programa