print("PIEDRA, PAPEL O TIJERA")

puntos_jugador = 0
puntos_compu = 0

import random
opc = ["piedra", "papel", "tijera"]

while True:
    print("Elige una opción:")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")
    print("4 - Salir")
    
    elegir_opc = input("elige (1 - 2 - 3 - 4): ")
    
    if elegir_opc == "4":
        
        print(" ")
        print(f"-PUNTOS JUGADOR: {puntos_jugador}")
        print(f"-PUNTOS COMPUTADORA: {puntos_compu}")
        
        if puntos_jugador > puntos_compu:
            
            print("FELICITACIONES!, GANASTE!!!!")
            
        elif puntos_jugador == puntos_compu:
            
            print("EMPATE")
            
        else:
            
            print("QUE PENA, GANO LA COMPUTADORA")
            
        print(" ")
        print("¡Gracias por jugar!")
        break  


    if elegir_opc not in ["1", "2", "3"]:
        print("ingrese un numero valido")
        continue



    jugador = opc[int(elegir_opc) - 1]
    compu = random.choice(opc)

    print(" ")
    print(f"-EL JUGADOR ELIGIO {jugador}")
    print(f"-LA COMPUTADORA ELIGIO {compu}")
    print(" ")

    if jugador == compu:
        
        print("EMPATE")
        
    elif (jugador == "tijera" and compu == "papel") or (jugador == "piedra" and compu == "tijera") or (jugador == "papel" and compu == "piedra"):
    
        print("<JUGADOR GANA>")
        puntos_jugador += 1
    
    elif (compu == "tijera" and jugador == "papel") or (compu == "piedra" and jugador == "tijera") or (compu == "papel" and jugador == "piedra"):
    
        print("<COMPUTADORA GANA>")
        puntos_compu += 1
        print(" ")