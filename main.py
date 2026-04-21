import random

def adivina_numero():
    print("¡Bienvenido a Adivina el Número!")
    numero_secreto = random.randint(1, 100) # lo subimos a 100 para que se mas divertido con 5 intentos 
    
    # 1. creamos variable para controlar los intentos
    intentos_maximos = 5
    intentos_realizados = 0
    ganó = False # esta variable nos dirá si adivinó o no 

    print(f"Tienes {intentos_maximos} intentos para adivinar el número secreto")

    # 2. el blucle: "mientras los intentos realizados sean menores al máximo..."
    while intentos_realizados < intentos_maximos:
        intento = int(input(f"Intentos {intentos_realizados + 1}: Adivina el número: "))
        intentos_realizados += 1 # sumamos uno al contador de intentos 
        
        if intento == numero_secreto:
            print(f"¡Felicidades!, adivinaste el número en {intentos_realizados} intentos.")
            ganó= True
            break #salimos del blucle porque ya gano
        else:
            #pista (esto lo hará el Aprendiz 4, 
            # pero por ahora un mensaje simple)
            print("No es ese número.")

    # 3. Mensaje de derrota (Tu responsabilidad)
    if not ganó:
        print(f"Lo siento, te has quedado sin intentos. El número secreto era {numero_secreto}.")    

if __name__ == "__main__":
    adivina_numero()
