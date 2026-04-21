import random

def adivina_numero():
    print("¡Bienvenido a Adivina el Número!")
    numero_secreto = random.randint(1, 10)

    while True:
        entrada = input("Adivina un número entre 1 y 10: ")

        try:
            intento = int(entrada)
            break
        except ValueError:
            print("Error: Debes ingresar solo números.")

    if intento == numero_secreto:
        print("¡Felicidades, adivinaste el número!")
    else:
        print(f"Fallaste. El número secreto era {numero_secreto}")

if __name__ == "__main__":
    adivina_numero()
