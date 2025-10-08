
import random

#FUNCIONES
def peliculas():
    peliculas = [
    "El Padrino",
    "Casablanca",
    "Ciudadano Kane",
    "La lista de Schindler",
    "Forrest Gump",
    "Inception (El origen)",
    "Interstellar",
    "Parasite",
    "Everything Everywhere All at Once",
    "Joker",
    "Toy Story",
    "El viaje de Chihiro",
    "Coco",
    "Shrek",
    "Spider-Man: Into the Spider-Verse",
    "Her",
    "La La Land",
    "El secreto de sus ojos",
    "Amélie",
    "Whiplash"]

    return random.choice(peliculas).lower()

def mostrar_estado(seleccionada, letra_adivinada):
    
    estado = ""
    print()
    print("ESTADO DE LA PALABBRA:")
    
    for letra in seleccionada:
        if letra == " ":
            estado += "  "
        elif letra in letra_adivinada:
            estado += letra + " "
        else:
            estado += "_ "
    return estado

#PRINCIPAL

print("JUEGO DEL AHORCADO")

seleccionada = peliculas()
letra_adivinada = []
intentos = 6

print()

print(seleccionada)
print(mostrar_estado(seleccionada, letra_adivinada))

while intentos > 0:
    
    print()
    
    print(f"Tienes {intentos} intentos")
    buscar_letra = input("Introduce una letra: ").lower()
    
    if len(buscar_letra) != 1:
        print()
        print("POR FAVOR, INTRODUCE SOLO UNA LETRA.")
        continue
    
    letra_adivinada.append(buscar_letra)
    
    
    if buscar_letra not in seleccionada:
        intentos -= 1
        print()
        print(f"La letra '{buscar_letra}' no está en la palabra.")

    if intentos == 0:
        print()
        print("¡Has perdido! La palabra era:", seleccionada.upper())
        break
    
    estado_actual = mostrar_estado(seleccionada, letra_adivinada)
    print(estado_actual)
    
    if "_" not in estado_actual:
        print("¡Felicidades! ¡Has ganado!")
        break