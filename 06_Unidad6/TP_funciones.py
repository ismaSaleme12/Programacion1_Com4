#Tp funciones - Ismael Saleme - Comision 4

#-----------------------------------------
#Ejercicio 1

#funcion 
def saludar():
    return("Hola, mundo!")

#principal
print("EJERCICIO 1")
saludo = saludar()
print(saludo)

#-----------------------------------------
#Ejercicio 2

#funcion
def saludar_nombre(nombre):
    return(f"Hola, {nombre}!")

#principal
print("EJERCICIO 2")
nombre = input("Ingrese su nombre: ")

print(saludar_nombre(nombre))

#-----------------------------------------
#Ejercicio 3

#funcion
def informacion_personal(nmb,apell,edad,resid):
    return(f"Soy {nmb} {apell}, tengo {edad} años y vivo en {resid}")

#principal
print("EJERCICIO 3")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))

#-----------------------------------------
#Ejercicio 4

#funcion
def calcular_area_circulo(radio):
    pi = 3.1416
    area = pi * (radio ** 2)
    return f"El area del circulo es: {area}"

def calcular_perimetro_circulo(radio):
    pi = 3.1416
    perimetro = 2 * pi * radio
    return f"El perimetro del circulo es: {perimetro}"


#principal
print("EJERCICIO 4")
radio = float(input("ingrese el radio del circulo: "))

print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))

#-----------------------------------------
#Ejercicio 5

#funcion
def segundos_a_horas(seg):
    horas = seg // 3600
    return f"{seg} segundos son {horas} horas"

#principal
print("EJERCICIO 5")
segundos = int(input("Ingrese la cantidad de segundos a: "))

print(segundos_a_horas(segundos))

#-----------------------------------------
#Ejercicio 6

#funcion
def tabla_multiplicar(num):
    print(f"TABLA DE MULTIPLICAR DEL {num}")
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

#principal
print("EJERCICIO 6")
numero = int(input("De que numero quiere saber la tabla de multiplicar?: "))

tabla_multiplicar(numero)

#-----------------------------------------
#Ejercicio 7

#funcion
def operaciones_basicas(n1,n2):
    
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    division = n1 / n2
    
    return (suma, resta, multiplicacion, division)

#principal
print("EJERCICIO 7")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(num1,num2)

print(f"La suma es: {resultados[0]}")
print(f"La resta es: {resultados[1]}")
print(f"La multiplicacion es: {resultados[2]}")
print(f"La division es: {resultados[3]}")
    

#-----------------------------------------
#Ejercicio 8

#funcion
def indice_masa_corporal(peso, altura):
    imc = peso / (altura ** 2)
    return imc

#principal
print("EJERCICIO 8")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

resultado_imc = indice_masa_corporal(peso, altura)

print(f"Su indice de masa corporal es de: {resultado_imc:2.2f}")

#-----------------------------------------
#Ejercicio 9

#funcion
def celsius_a_fahrenheit(cel):
    fahrenheit = (cel * 9/5) + 32
    return fahrenheit

#principal
print("EJERCICIO 9")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

resultado = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius son {resultado} grados Fahrenheit")

#-----------------------------------------
#Ejercicio 10

#funcion
def calcular_promedio(n1,n2,n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio

#principal
print("EJERCICIO 10")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

resultado = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres numeros es: {resultado:2.2f}")
