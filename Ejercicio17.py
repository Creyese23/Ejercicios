#Diseñe un algoritmo que dada una fecha, calcule el número de días que
# han transcurrido desde el inicio del año.
while True:
    from datetime import datetime 
    # Solicitar al usuario que introduzca una fecha
    fecha = input("Introduce una fecha (DD/MM/AAAA): ")
    fecha_fin = datetime.strptime(fecha, "%d/%m/%Y")
    try:
        # Dividir la fecha en día, mes y año
        dia, mes, anio = map(int, fecha.split('/'))

        # Verificar si el año es bisiesto
        def es_bisiesto(año):
            return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

            # Calcular el número de días transcurridos desde el inicio del año
        dias_transcurridos = 0
        dias_transcurridos += dia  # Días del mes actual
        for m in range(1, mes):
            if m in [1, 3, 5, 7, 8, 10, 12]:  # Meses con 31 días
                dias_transcurridos += 31
            elif m in [4, 6, 9, 11]:  # Meses con 30 días
                dias_transcurridos += 30
            elif m == 2:  # Febrero
                if es_bisiesto(anio):
                    dias_transcurridos += 29
                else:
                    dias_transcurridos += 28

        # Imprimir el resultado
        print(f"Desde el inicio del año, han transcurrido {dias_transcurridos} días.")
    except ValueError:
        print("Por favor, ingrese una fecha válida en el formato DD/MM/AAAA.")
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar == 's':
        continue