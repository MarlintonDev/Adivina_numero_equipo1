import random

def adivina_numero():
    while True:
        print("\n¡Bienvenido a Adivina el Número!")
        numero_secreto = random.randint(1, 10)
        intentos_maximos = 3
        ganado = False

        for i in range(intentos_maximos):
            try:
                intento = int(input(f"Intento {i+1}/{intentos_maximos} - Adivina un número entre 1 y 10: "))
                
                if intento == numero_secreto:
                    print("¡Felicidades, adivinaste el número!")
                    ganado = True
                    break
                elif intento < numero_secreto:
                    print("Pista: El número es mayor.")
                else:
                    print("Pista: El número es menor.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        # Mensaje final de victoria o derrota
        if not ganado:
            print(f"¡Derrota! Te has quedado sin intentos. El número secreto era {numero_secreto}.")
        
        # Opción de reiniciar el juego
        reiniciar = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if reiniciar != 's':
            print("¡Gracias por jugar! Hasta luego.")
            break

if __name__ == "__main__":
    adivina_numero()
