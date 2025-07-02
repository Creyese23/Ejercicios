#Codigo para realizar e imprimir el resultado de las operaciones de 2 nummeros
while True:
    # Menú de opciones
    print("----------")
    print("|Menu: |")
    print("|+ Suma|")
    print("|- Resta|")
    print("|* Multiplicación|")
    print("|/ División|")
    print("----------")
    
    # Solicitar al usuario que ingrese dos números
    try:
        num = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))

        op = input("Ingrese la operacion a realizar (+, -, *, /): ")

        if op == "+":
            suma = num + num2
            print(f"El resultado de {num} + {num2} es: {suma}")
        elif op == "-":
            resta = num - num2
            print(f"El resultado de {num} - {num2} es: {resta}")
        elif op == "*":
            Mult = num * num2
            print(f"El resultado de {num} * {num2} es: {Mult}")
        elif op == "/":
            if num2 != 0:
                Div = num / num2
                print(f"El resultado de {num} / {num2} es: {Div}")
            elif num2 == 0:
                result = 0
                print(f"El resultado es: {result}")
        else:
            print("Operación no válida. Por favor, elige una de las opciones del menú.")
            break  # Salir del bucle si la entrada es válida
        
        # Preguntar al usuario si desea continuar
        continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saliendo del programa.")
            break
    except ValueError:
        print("Entrada no válida. Por favor, introduce números enteros.")
        continue
# Fin del programa
# Este código permite al usuario realizar operaciones matemáticas básicas entre dos números.