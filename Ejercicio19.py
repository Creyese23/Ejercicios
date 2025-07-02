#Una modista para realizar sus prendas de vestir, encarga las telas al exterior. Para
#cada pedido tiene que proporcionar las medidas de la tela en pulgadas, pero ella
#generalmente las tiene en metros. Realice un algoritmo para ayudar a resolver el
#problema, determinando cuantas pulgadas debe pedir con base en los metros que
#requiere. Represéntelo mediante seudocódigo. (1 pulgada = 0,0254m)

# Conversión de metros a pulgadas
# 1 pulgada = 0.0254 metros
while True:
    metros = input("Introduce la cantidad de metros que necesitas: ")

    try:

        metros = float(metros)
        pulgadas = metros / 0.0254
        print(f"Para {metros} metros, debes pedir {pulgadas:.2f} pulgadas de tela.")
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

# Fin del programa
# Este programa solicita al usuario la cantidad de metros de tela que necesita y calcula