import random

def adivina_numero():

    print("¡Bienvenido a Adivina el Número!")
    numero_secreto = random.randint(1, 100)  # lo subimos a 100 para que sea más divertido con 5 intentos 
    while True:
        entrada = input("Adivina un número entre 1 y 100: ")

        try:
            intento = int(entrada)
            break
        except ValueError:
            print("Error: Debes ingresar solo números.")

    if intento == numero_secreto:
        print("¡Felicidades, adivinaste el número!")
    else:
        print(f"Fallaste. El número secreto era {numero_secreto}")
    # 1. creamos variable para controlar los intentos
    intentos_maximos = 5
    intentos_realizados = 0
    ganó = False # esta variable nos dirá si adivinó o no 

    print(f"Tienes {intentos_maximos} intentos para adivinar el número secreto")

    # 2. el blucle: "mientras los intentos realizados sean menores al máximo..."
    while intentos_realizados < intentos_maximos:
        try:
            intento = int(input(f"Intentos {intentos_realizados + 1}: Adivina el número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        intentos_realizados += 1  # sumamos uno al contador de intentos 
        
        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos_realizados} intentos.")
            ganó = True
            break  # salimos del bucle porque ya ganó
        else:
            if intento < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")

     
   # Mensaje final de victoria o derrota
        if not ganado:
            print(f"¡Derrota! Te has quedado sin intentos. El número secreto era {numero_secreto}.")
        
        # Opción de reiniciar el juego
        reiniciar = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if reiniciar != 's':
            print("¡Gracias por jugar! Hasta luego.")
            break
 main

if __name__ == "__main__":
    adivina_numero()
