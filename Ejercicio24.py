#Introducir tantas frases como queramos y contarlas.

# Hacer un pseudocódigo que imprima las frases introducidas y cuente cuántas hay.

#Vector de frases para almacenar las frases introducidas.
frases = []
while True:
    frase = input("Ingrese una frase (o 'salir' para terminar): ")
    if frase.lower() == 'salir':
        break
    frases.append(frase)

    print("Frases introducidas:")
    for i, frase in enumerate(frases, start=1):
        print(f"{i}: {frase}")
    print(f"Total de frases introducidas: {len(frases)}")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar != 's':
        print("Entrada no válida. Por favor, ingrese 's' para continuar o 'n' para salir.")
        break
# Fin del pseudocódigo