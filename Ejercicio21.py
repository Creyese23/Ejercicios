#Una empresa que contrata personal requiere determinar la edad de las personas
#que solicitan trabajo, pero cuando se les realiza la entrevista solo se les pregunta
#el año en que nacieron. Realice el seudocódigo para solucionar el problema.

from datetime import datetime
while True:
    anio = input("Ingrese el año de nacimiento: ")
    anio_actual = datetime.now().year

    try: 
        anio = int(anio)
        # Calcular la edad
        edad = anio_actual - anio

        print(f"La edad de la persona es: {edad} años")
    except ValueError:
        print("Por favor, ingrese un año válido.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar != 's':
        print("Entrada no válida. Por favor, ingrese 's' para continuar o 'n' para salir.")
        break
# Fin del programa