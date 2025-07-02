#Introducir dos números por teclado. Imprimir los números naturales que hay entre
#ambos números empezando por el mas pequeño, contar cuantos hay y cuántos
#de ellos son pares. Calcular la suma de los impares.

# Pseudocódigo para introducir dos números y procesar los números naturales entre ellos 
while True:
    num1 = input("Introduce el primer número: ")
    num2 = input("Introduce el segundo número: ")

    try:
        num1 = int(num1)
        num2 = int(num2)
        # Determinar el menor y el mayor de los dos números
        if num1 < num2:
            menor = num1
            mayor = num2
        else:
            menor = num2
            mayor = num1

        # Inicializar contadores y suma
        contador = 0
        suma_impares = 0
        pares = 0

        # Imprimir los números naturales entre menor y mayor
        print(f"Números naturales entre {menor} y {mayor}:")
        for i in range(menor + 1, mayor):
            print(i, end=' ')
            contador += 1  # Contar los números
            if i % 2 == 0:
                pares += 1  # Contar los pares
            else:
                suma_impares += i  # Sumar los impares
            print("\n")
        # Imprimir resultados
        print(f"Cantidad de números naturales entre {menor} y {mayor}: {contador}")
        print(f"Cantidad de números pares: {pares}")
        print(f"Suma de los números impares: {suma_impares}")
    except ValueError:
        print("Por favor, introduce números válidos.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar != 's':
        print("Entrada no válida. Por favor, ingrese 's' para continuar o 'n' para salir.")
        break
        