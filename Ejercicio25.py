#Hacer un Pseudocodigo que imprima los números del 1 al 100. Que calcule la
#suma de todos los números pares por un lado, y por otro, la de todos los impares.

# Pseudocódigo para imprimir números del 1 al 100 y calcular sumas de pares e impares
# Iniciar suma de números pares e impares en 0
suma_pares = 0
suma_impares = 0

while True:
    num = input("Introduce un número: ")
    try: 
        num = int(num)   
        # Para cada número del 1 al número ingresado
        for numero in range(1, num+1):
            # Imprimir el número actual
            print(numero)
    
            # Si el número es par, añadirlo a la suma de pares
            if numero % 2 == 0:
                suma_pares += numero
                # Si el número es impar, añadirlo a la suma de impares
            else:
                suma_impares += numero

        # Imprimir las sumas finales
        print(f"Suma de números pares: {suma_pares}")
        print(f"Suma de números impares: {suma_impares}")
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
# Fin del pseudocódigo