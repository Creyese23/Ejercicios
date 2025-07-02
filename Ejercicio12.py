#Escribir un programa que lea tres números enteros por teclado y emita un mensaje indicando si están o no ordenados crecientemente.
while True:
    # Solicitar al usuario que ingrese tres números enteros
    numero1 = int(input("Ingrese el primer número entero: "))
    numero2 = int(input("Ingrese el segundo número entero: "))
    numero3 = int(input("Ingrese el tercer número entero: "))
    try: 
        # Verificar si los números están ordenados crecientemente
        if numero1 < numero2 < numero3:
            print("Los números están ordenados crecientemente.")
        else:
            print("Los números no están ordenados crecientemente.")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar == 's':
        continue
# Fin del programa
# Este programa solicita al usuario tres números enteros y verifica si están en orden creciente.