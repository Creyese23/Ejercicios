#Diseñe un algoritmo que permita calcular el día siguiente de una fecha:

def dia_siguiente(dia, mes, anio):
    # Días por mes considerando año bisiesto
    dias_por_mes = [31, 28 + (1 if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia += 1
    if dia > dias_por_mes[mes - 1]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return dia, mes, anio

while True:
    try:
        # Código para calcular el día siguiente de una fecha
        dia = int(input("Ingrese el día (DD): "))
        mes = int(input("Ingrese el mes (MM): "))
        anio = int(input("Ingrese el año (AAAA): "))
        # Días por mes considerando año bisiesto
        dias_por_mes = [31, 28 + (1 if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        # Incrementar el día
        dia += 1
    
        # Verificar si el día supera el número de días del mes
        if dia > dias_por_mes[mes - 1]:
                dia = 1
                mes += 1
        
                # Verificar si el mes supera diciembre
        if mes > 12:
                mes = 1
                anio += 1
            
            
        # Solicitar la fecha al usuario
                dia = int(input("Ingrese el día (DD): "))
                mes = int(input("Ingrese el mes (MM): "))
                anio = int(input("Ingrese el año (AAAA): "))
                # Validar la fecha ingresada
                if (1 <= mes <= 12 and 1 <= dia <= 31):
                        if (mes == 2 and dia > 29) or (mes in [4, 6, 9, 11] and dia > 30):
                            print("Fecha no válida. Verifique el día del mes.")
                        else:
                            # Calcular el día siguiente
                            dia_siguiente_resultado = dia_siguiente(dia, mes, anio)
                            print(f"El día siguiente es: {dia_siguiente_resultado[0]:02d}/{dia_siguiente_resultado[1]:02d}/{dia_siguiente_resultado[2]}")
                else:
                        print("Fecha no válida. Mes o día fuera de rango.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce números enteros para el día, mes y año.")
        continue
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saliendo del programa.")
        break