#Hacer un pseudocodigo que simule el funcionamiento de un reloj digital y que
#permita ponerlo en hora.

# Pseudocódigo para simular un reloj digital y permitir ponerlo en hora

# Inicializar horas, minutos y segundos
horas = 0
minutos = 0
segundos = 0

# Función para mostrar la hora en formato digital
def mostrar_hora():
    print(f"{horas:02}:{minutos:02}:{segundos:02}")

# Función para poner el reloj en hora
def poner_en_hora():
    global horas, minutos, segundos
    horas = int(input("Introduce las horas (0-23): "))
    minutos = int(input("Introduce los minutos (0-59): "))
    segundos = int(input("Introduce los segundos (0-59): "))
    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59 or segundos < 0 or segundos > 59:
        print("Hora no válida. Inténtalo de nuevo.")
        poner_en_hora()
    else:
        print("Reloj puesto en hora correctamente.")

# Bucle principal para simular el reloj
while True:
    mostrar_hora()  # Mostrar la hora actual
    accion = input("¿Deseas poner el reloj en hora? (s/n): ").lower()
    
    if accion == 's':
        poner_en_hora()  # Poner el reloj en hora
    elif accion == 'n':
        # Incrementar los segundos
        segundos += 1
        if segundos == 60:
            segundos = 0
            minutos += 1
            if minutos == 60:
                minutos = 0
                horas += 1
                if horas == 24:
                    horas = 0
    else:
        print("Opción no válida. Inténtalo de nuevo.")
    
    # Esperar un segundo antes de continuar (simulación)
    import time
    time.sleep(1)

# Fin del pseudocódigo
# Nota: Este pseudocódigo es una simulación y no se ejecutará como un programa