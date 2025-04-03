import random

def lanzar_dados():
    # Genera dos números aleatorios entre 1 y 6
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def jugar_monopoly():
    intentos = 0

    while True:
        dado1, dado2 = lanzar_dados()
        print(f"Has sacado: {dado1} y {dado2}")

        if dado1 == dado2:
            intentos += 1
            print("perro qlo con suerte!!! juegue.")
            if intentos == 3:
                print("PA CANA MI SHAN!")
                break
        else:
            print("Turno finalizado.")
            break
resultado = jugar_monopoly()
while True:
    jugar_monopoly()
    opcion = input("¿Quieres volver a tirar los dados? (s/n): ").strip().lower()
    if opcion == 'n':  # Si elige 'n', termina el juego
        print("Juego terminado.")
        break
    elif opcion != 's':  # Si no es 's' ni 'n', muestra un mensaje de error
        print("Opción no válida. Por favor, ingresa 's' para sí o 'n' para no.")