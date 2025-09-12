

print("-----------------------------------------------------------------------")

print()
print("EJERCICIO 1")

lista_numero = []

#NUMEROS DEL 1 AL 100 Y VERIFICACION SI ES MULTIPLO DE 4
for i in range(1,101):
    if i % 4 == 0:
        lista_numero.append(i)

print(lista_numero)

print()
print("-----------------------------------------------------------------------")


print()
print("EJERCICIO 2")

lista_elementos = ["papa", 4, True, "UTN", 4500]

#INDEXING NEGATIVO. 
print(lista_elementos[-2] )


print()
print("-----------------------------------------------------------------------")



print()
print("EJERCICIO 3")

lista = []

#AGREGO STRING A LA LISTA
lista.append("verduras")
lista.append("carne")
lista.append("picada")

print(lista)


print()
print("-----------------------------------------------------------------------")


print()
print("EJERCICIO 4")

animales = ["perro", "gato", "conejo", "pez"]

#LISTA ORIGINAL
print()
print("-lista original")
print(animales)

animales[1] = "loro"
animales[3] = "oso"

#LISTA CON VALORES 1 Y 3 MODIFICADOS
print()
print("-lista modificada")
print(animales)


print()
print("-----------------------------------------------------------------------")



print()
print("EJERCICIO 5")

#CODIGO PARA ANALIZAR

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#Lo que hace este bloque de codigo es eliminar el valor maximo de la lista "numeros". Primero se ingresan los valores de la lista y segundo se llama a la funcion "remove", la cual va a eliminar el valor maximo de la lista. Este valor se encuentra usando la funcion "max". Finalmente, se muestra en pantalla el resultado del codigo. 
#En este caso, se eliminaria el numero 22


print()
print("-----------------------------------------------------------------------")



print()
print("EJERCICIO 6")

lista_numeros = []

#AGREGO NUMEROS DEL 10 AL 30 CON PASO 5 A LA LISTA
for i in range (10,31,5):
    lista_numeros.append(i)

#MUESTRO LOS DOS PRIMEROS ELEMENTOS
print()
print("PRIMER ELEMENTO")
print(lista_numeros[0])

print()
print("SEGUNDO ELEMENTO")
print(lista_numeros[1])


print()
print("-----------------------------------------------------------------------")


print()
print("EJERCICIO 7")

autos = ["sedan", "polo", "suran", "gol"]

print()
print("original")
print(autos)

#MODIFICO LOS VALORES 1 Y 2 DE LA LISTA "AUTOS"
autos[1] = "camioneta"
autos[2] = "bicicleta"

print()
print("modificada")
print(autos)


print()
print("-----------------------------------------------------------------------")


print()
print("EJERCICIO 8")

dobles = []

#INGRESO LOS VALORES: 5,10 Y 15
for i in range(5,16,5):
    dobles.append(i*2) # MULTIPLICO *2 EL VALOR DE "i"


print(dobles)


print()
print("-----------------------------------------------------------------------")



print()
print("EJERCICIO 9")

lista_compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

print()
print("original")
print(lista_compras)

#MODIFICACION DE VALORES
lista_compras[2].append("jugo")    #AGREGO
lista_compras[1][1] = "tallarines" #MODIFICO
lista_compras[0].remove("pan")     #ELIMINO

print()
print("modificada")
print(lista_compras)


print()
print("-----------------------------------------------------------------------")


print()
print("EJERCICIO 10")


lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)