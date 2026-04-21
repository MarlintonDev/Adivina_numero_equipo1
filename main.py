import random

def adivina_numero():
    print("¡Bienvenido a Adivina el Número!")
    numero_secreto = random.randint(1, 100)  # lo subimos a 100 para que sea más divertido con 5 intentos 
    
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

    # 3. Mensaje de derrota 
    if not ganó:
        print(f"Lo siento, te has quedado sin intentos. El número secreto era {numero_secreto}.")    

if __name__ == "__main__":
    adivina_numero()
