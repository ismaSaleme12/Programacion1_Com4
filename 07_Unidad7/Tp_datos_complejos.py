#Practico 7 - estructura de datos complejas

#------------------------------------------
#Ejercicio 1

precio_frutas = {"banana": 1200, "anana": 2500, "melon": 3000, "uva": 1450}

#Agrego nuevas frutas
precio_frutas["naranja"] = 1200
precio_frutas["manzana"] = 1500
precio_frutas["pera"] = 2300

print(precio_frutas)


#------------------------------------------
#Ejercicio 2

precio_frutas["banana"] = 1330
precio_frutas["manzana"] = 1500
precio_frutas["melon"] = 2300

print(precio_frutas)

#------------------------------------------
#Ejercicio 3

lista_frutas = list(precio_frutas.keys())

print(lista_frutas)

#------------------------------------------
#Ejercicio 4

telefonos = {}

for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    numero = input(f"Ingresa el numero del contacto {nombre}: ")

    telefonos[nombre] = numero

print(telefonos)

#------------------------------------------
#Ejercicio 5


frase = input("ingresa una frase: ")

palabras = frase.split()

recuento = {}

for palabra in palabras:

    if palabra in recuento:
        recuento[palabra] += 1

    else:
        recuento[palabra] = 1


print("Palabras unicas: ", set(palabras))
print("Recuento de palabras: ", recuento)

#------------------------------------------
#Ejercicio 6

alumnos = {}

for i in range(3):
    alumno = input(f"Ingresa el nommbre del alumno {i+1}: ")
    notas = []

    for nota in range(3):
        nota = input(f"Ingresa la nota {nota+1}: ")
        notas.append(nota)


        alumnos[alumno] = tuple(notas)


print(alumnos)

#------------------------------------------
#Ejercicio 7



parcial1 = {1,2,3,4,5}
parcial2 = {4,5,6,7}

#aprbados ambos parciales
ambos = parcial1 & parcial2 
print(ambos)

#aprobado solo uno
solo_uno = parcial1 ^ parcial2
print(solo_uno)

#aporbados al menos uno
total = parcial1 | parcial2
print(total)

#------------------------------------------
#Ejercicio 8

productos = {"galletas": 120, "gaseosas": 45, "tortitas": 89}


while True:

    print("--------------------------")
    print("PRODUCTOS\n")

    print("|1| Consultar stock")
    print("|2| Agregar stock")
    print("|3| Agregar producto")
    print("|4| Salir")

    opc = input("Cual opcion eliges?: ")


    match opc:

        case "1":     
            consultar = input("De cual producto quieres saber el stock?: ").lower()

            if consultar in productos:
                print(f"Stock de {consultar}: {productos[consultar]}")
            else:
                print("El producto no esta cargado en el sistema")

        case "2": 
            renovar_stock = input("Que producto quieres renovar?: ").lower()

            if renovar_stock in productos:
                nuevo_stock = input("¿Cual es el nuevo stock del producto?: ")

                productos[renovar_stock] = int(nuevo_stock)
            else:
                print("EL producto ingresado no esta en el sistema")

        case "3":
            agregar_nuevo = input("¿Como se llama el producto que quieres agregar?: ").lower()

            if not agregar_nuevo in productos:

                stock_producto_nuevo = input("¿Cual es el stock del producto?: ")

                productos[agregar_nuevo] = int(stock_producto_nuevo)

            else:
                print("El producto ya se encuentra en el sistema")

        case "4":
            break

#------------------------------------------
#Ejercicio 9

agenda = {

    ("lunes", "10:00"): "Arquitectura en SO",
    ("martes", "8:00"): "Matematicas",
    ("miercoles", "11:00"): "Asincronico programacion",
    ("jueves", "8:45"): "Programacion",
    ("viernes", "9:45"): "organizacion empresarial"
}

dia = input("¿Que dia quere consultar?: ")
horario = input("¿Que horario? (formato HH:MM): ")

clave_dict = (dia,horario)

if clave_dict in agenda:
    print(f"Actividad programada: {agenda[clave_dict]}")

else:
    print("no hay actividad en ese horario")


#------------------------------------------
#Ejercicio 10

#Diccionario original

paises = {
    "Namibia": "Windhoek",
    "Eslovenia": "Liubliana",
    "Sri Lanka":  "Sri Jayawardenapura Kotte",
    "Guatemala":  "Ciudad de Guatemala",
    "Armenia":  "Ereván"
}

#Diccionario invertido

invertido = {
    "Windhoek": "Namibia",
    "Liubliana": "Eslovenia",
    "Sri Jayawardenapura Kotte": "Sri Lanka",
    "Ciudad de Guatemala": "Guatemala",
    "Ereván": "Armenia"
}