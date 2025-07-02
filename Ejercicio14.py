#Construya un pseudocódigo tal que dados como datos la matricula y 
# 5 calificaciones de un alumno; imprima los datos de matrícula, el promedio y la
# palabra “aprobado” si el alumno tiene un promedio mayor o igual a 7.5 y la palabra
# “reprobado” en caso contrario.
while True:
    # Pseudocódigo para calcular el promedio de un alumno y determinar si está aprobado o reprobado
    nota1, nota2, nota3, nota4, nota5 = 0, 0, 0, 0, 0
    promedio = 0

    # Solicitar la matrícula del alumno
    matricula = input("Ingrese la matrícula del alumno: ")
    try:
        matricula = int(matricula)
        # Solicitar las calificaciones del alumno
        nota1 = float(input("Ingrese la calificación 1 del alumno: "))
        nota2 = float(input("Ingrese la calificación 2 del alumno: "))
        nota3 = float(input("Ingrese la calificación 3 del alumno: "))
        nota4 = float(input("Ingrese la calificación 4 del alumno: "))
        nota5 = float(input("Ingrese la calificación 5 del alumno: "))

        # Calcular el promedio de las calificaciones
        promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

        # Imprimir los resultados
        if promedio >= 7.5:
            print(f"Matrícula: {matricula}")
            print(f"Promedio: {promedio:.2f}")
            print("Aprobado")
        else:
            print(f"Matrícula: {matricula}")
            print(f"Promedio: {promedio:.2f}")
            print("Reprobado")
    except ValueError:
        print("Por favor, ingrese una matrícula válida.")
        continue
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    if continuar == 'n':
        print("Saliendo del programa.")
        break
    elif continuar == 's':
        continue
# Fin del programa
# Este programa solicita la matrícula y cinco calificaciones de un alumno, calcula el promedio y determina