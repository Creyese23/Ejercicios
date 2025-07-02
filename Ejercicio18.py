#Realice un programa que permita obtener una estructura similar a la siguiente: 
# *********
# *******
# *****
# ***
# * 
# Donde el número de asteriscos por línea se obtiene de un número introducido por teclado.

while True:
    # Solicitar al usuario que introduzca un número
    numero = input("Introduce un número para generar el patrón de asteriscos: ")

    try:
        numero = int(numero)
        # Validar que el número es positivo
        if numero <= 0:
            print("Por favor, introduce un número positivo.")
        else:
        # Generar el patrón de asteriscos
            for i in range(numero, 0, -2):
                print('*' * i)
                #print()
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar == 's':
        continue

# Fin del programa
# Este programa imprime una serie de líneas con un número decreciente de asteriscos,