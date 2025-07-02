#Calcular el factorial de un numero.
while True:
    # Introducir un número por teclado y calcular su factorial.
    numero = input("Introduce un número para calcular su factorial: ")
    factorial = 1
    try:
        numero = int(numero)
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es: {factorial}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar == 's':
        continue