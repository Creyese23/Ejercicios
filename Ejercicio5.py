#Codigo para imprimir aumento incorporado, categoria y tiempo de servicio
while True:
    salario = float(input("Ingrese el salario del empleado: "))
    categoria = input("Ingrese la categoria del empleado (A, B, C, D): ").upper()
    tiempo_servicio = int(input("Ingrese el tiempo de servicio del empleado en años: "))

    try:
        if categoria == "A":
            aumento = salario * 1.15
            aumento = round(aumento, 2)  # Redondear a dos decimales

            print(f"El salario original es: {salario}")
            print(f"El aumento para la categoria A es: {categoria}")
            print(f"El nuevo salario es: {aumento}")
            print(f"Tiempo de servicio: {tiempo_servicio} años")
        elif categoria == "B":
            aumento = salario * 1.12
            aumento = round(aumento, 2)
            print(f"El salario original es: {salario}")
            print(f"El aumento para la categoria B es: {categoria}")
            print(f"El nuevo salario es: {aumento}")
            print(f"Tiempo de servicio: {tiempo_servicio} años")
        elif categoria == "C":
            aumento = salario * 1.10
            aumento = round(aumento, 2)
            print(f"El salario original es: {salario}")
            print(f"El aumento para la categoria C es: {categoria}")
            print(f"El nuevo salario es: {aumento}")
            print(f"Tiempo de servicio: {tiempo_servicio} años")
        elif categoria == "D":
            aumento = salario * 1.15
            aumento = round(aumento, 2)
            print(f"El salario original es: {salario}")
            print(f"El aumento para la categoria D es: {categoria}")
            print(f"El nuevo salario es: {aumento}")
            print(f"Tiempo de servicio: {tiempo_servicio} años")
        else:
            aumento = 0
            print("Categoria no valida. No se aplicara aumento.")

        # Preguntar al usuario si desea continuar
        continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saliendo del programa.")
            break
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número válido para el salario y un entero para el tiempo de servicio.")
        continue