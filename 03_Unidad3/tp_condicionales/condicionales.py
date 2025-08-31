#tp condicionales - Saleme, Ismael


#EJERCICIO 1
print(" ")
print("EJERCICIO 1")

#ingreso de datos
edad= int(input("Ingrese su edad: "))

if edad >= 18:
    print("es mayor de edad")
    
#EJERCICIO 2
print(" ")
print("EJERCICIO 2")

#ingreso de datos
nota= int(input("Ingrese su nota: "))

#validacion y salida
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    

#EJERCICIO 3
print(" ")
print("EJERCICIO 3")

#ingreso de datos
num= int(input("ingrese un numero par: "))

#validacion y salida
if num % 2 == 0:
    print("ha ingresado un numero par")
else:
    print("por favor, ingrese un numero par")
    
    
#EJERCICIO 4
print(" ")
print("EJERCICIO 4")

#ingreso de datos
edad = int(input("Ingrese su edad: "))

#verificacion de categoria 
if edad < 12:
    categoria = "niño/a"
elif edad >= 12 and edad < 18:
    categoria = "adolescente"
elif edad >= 18 and edad < 30:
    categoria = "adulto/a joven"
else:
    categoria = "adulto/a"
        
print("Usted pertenece a la categoria", categoria)

#EJERCICIO 5
print(" ")
print("EJERCICIO 5")

#ingreso de datos
contraseña = input("Ingrese su contraseña: ")

#verificacion de longitud
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("ha ingresado una contraseña valida")
else:
    print("Por favor, ingrese una contraseñade entre 8 y 14 caracteres")
    
    
#EJERCICIO 6
print(" ")
print("EJERCICIO 6")

#importacion de librerias
from statistics import mode, median, mean 
import random

#ingreso de datos
numeros = [random.randint(1, 100) for i in range (50)]

#sesgo positivo, negativo o sin sesgo
if mean(numeros) > median(numeros) and median(numeros) > mode(numeros):
    print("Sesgo positivo")
elif mean(numeros) < median(numeros) and median(numeros) < mode(numeros):
    print("Sesgo negativo")
else:
    print ("sin sesgo")
    
#EJERCICIO 7
print(" ")
print("EJERCICIO 7")

#guardo las vocales en una tupla
vocales = "a", "e", "i", "o", "u"

#ingreso de datos
frase = input("Ingrese una frase: ")

#verificacion de la ultima letra
if frase[len(frase)-1].lower() in vocales:
    frase = frase + "!"
    print(frase)
else:
    print(frase)
    
#EJERCICIO 8
print(" ")
print("EJERCICIO 8")

#ingreso de datos
nombre = input("Ingrese su nombre: ")
num_opc = int(input("<1> nombre en mayusculas / <2> nombre en minusculas / <3> primer letra en mayuscula: "))

#verificacion de la opcion
if num_opc == 1:
    print(nombre.upper())
elif num_opc == 2:
    print(nombre.lower())
else:
    print(nombre.title())
    
#EJERCICIO 9
print(" ")
print("EJERCICIO 9")

#ingreso de datos
magnitud = float(input("ingrese la magnitud del terremoto: "))

#verificacion de la categoria de la magbitud del terremoto
if magnitud < 3:
    print("muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("leve (ligeramente percibido)")
elif magnitud >= 4 and magnitud < 5:
    print("moderado (sentido por personas pero no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("fuerte (puede causar daños a estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("muy fuerte (puede causar daños fuertes)")
else:
    print("extremo (puede causar daños graves)")
    
    
#EJERCICIO 10
print(" ")
print("EJERCICIO 10")

#ingreso de datos
hemisferio = input("Ingrese su hemisferio (Norte/Sur): ").lower()
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes (en numero): "))

#validacion de fecha incorrectas
if (mes < 1 or mes > 12) or (dia < 1 or dia > 31) or (mes == 2 and dia > 29) or (mes in [4,6,9,11] and dia > 30):
    print("Fecha no valida")
    exit() 
    
#hemisferios y estaciones
if hemisferio == "norte":
    
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
        
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
        
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
        
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha no valida"
        
elif hemisferio == "sur": 
    
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
        
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
        
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
        
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha no valida"
        
print("Se encuentra en la estacion de", estacion)