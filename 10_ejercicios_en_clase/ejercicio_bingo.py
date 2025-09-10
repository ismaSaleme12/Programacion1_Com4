#EJERCICIO BINGO    
#ISMAEL SALEME

import random

numeros = random.sample(range(1,51),25)

filas = 5
columnas = 5

carton = []
indice = 0

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(numeros[indice])
        indice += 1
    carton.append(fila)

#carton original
print("Carton bingo")
for fila in carton:
    print(fila)


#sorteo de numeros
numero_aleatorio = random.sample(range(1,51),50)
print(f"numero sorteado: {numero_aleatorio}")


#marcar el numero

contador = 25

for numero in numero_aleatorio:
    print(f"numero sorteado: {numero}")
    
    for i in range(filas):
        for j in range(columnas):
            if carton[i][j] == numero:
                carton[i][j] = 0
                contador -= 1
                
                print(" ")
                print("Tienes el numero")
                for fila in carton:
                    print(fila)
    
    if contador == 0:
        print("CARTON LLENO")
        break