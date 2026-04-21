import random

def adivina_numero():
    print("¡Bienvenido a Adivina el Número!")
    numero_secreto = random.randint(1, 10)
    
    intento = int(input("Adivina un número entre 1 y 10: "))
    
    if intento == numero_secreto:
        print("¡Felicidades, adivinaste el número!")
    else:
        print(f"Fallaste. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    adivina_numero()
