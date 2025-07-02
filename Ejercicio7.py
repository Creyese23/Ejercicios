#Diseñe un algoritmo que ingresada una fecha DD MM AA, reporte la fecha como: 
# “Es DD del mes de MM del año AAAA”, debe suponerse que la fecha ingresada
# es válida ejemplo: o1/03/2019 “es 01 del mes de marzo del año 2019”.
while True:
    # Codigo para imprimir la fecha en el formato solicitado
    dia = input("Ingrese el dia (DD): ")
    mes = input("Ingrese el mes (MM): ")
    anio = input("Ingrese el año (AA): ")
    try:
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)
        # Asegurarse de que el año tenga dos dígitos
        # Convertir el mes de MM a su nombre correspondiente
        meses = {
            "01": "enero",
            "02": "febrero",
            "03": "marzo",
            "04": "abril",
            "05": "mayo",
            "06": "junio",
            "07": "julio",
            "08": "agosto",
            "09": "septiembre",
            "10": "octubre",
            "11": "noviembre",
            "12": "diciembre"
        }
        if mes in meses:
            mes_nombre = meses[mes]

            # Convertir el año de AA a AAAA
            if len(anio) == 2:
                anio_completo = "20" + anio  # Asumiendo que es del siglo XXI
            else:
                anio_completo = anio
                print(f"Es {dia} del mes de {mes_nombre} del año {anio_completo}.")
        else:
            print("Mes no válido. Debe estar entre 01 y 12.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce números enteros para el día y el mes.")
        continue
        # Preguntar al usuario si desea continuar
        continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saliendo del programa.")
            break