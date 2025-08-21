#Trabajo Practico 1 - Saleme, Ismael 

#Ejercicio 1

print("Hola, mundo")

#Ejercicio 2
print(" ")
print("--------------------------------------")

nombre=input("Escribe tu nombre: ")
print(f"Hola, {nombre}, ¿como estas?")

#Ejercicio 3

print(" ")
print("--------------------------------------")

nombre=input("Escribe tu nombre: ")
apellido=input("Escribe tu apellido: ")
edad=int(input("Escribe tu edad: "))
ciudad=input("dime tu lugar de residencia:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad}")

#Ejercicio 4

print(" ")
print("--------------------------------------")

pi=3.1416
radio=float(input(" dime el radio: "))

area=pi*radio**2
perimetro=2*pi*radio

print(f"El area del circulo es {area}")
print(f"El perimetro del circulo es de {perimetro}")

#Ejercicio 5

print(" ")
print("--------------------------------------")

segundos=int(input(" dime los segundos: "))
horas=segundos//3600

print(f"{segundos} segundos equivalen a {horas} hora/s")

#Ejercicio 6

print(" ")
print("--------------------------------------")

num=input(" dime el numero que quieres multiplicar:")

print(f"<Tabla del {num}>")

print(f"{num} x 1 = {int(num)*1}")
print(f"{num} x 2 = {int(num)*2}")
print(f"{num} x 3 = {int(num)*3}")
print(f"{num} x 4 = {int(num)*4}")
print(f"{num} x 5 = {int(num)*5}")
print(f"{num} x 6 = {int(num)*6}")
print(f"{num} x 7 = {int(num)*7}")
print(f"{num} x 8 = {int(num)*8}")
print(f"{num} x 9 = {int(num)*9}")
print(f"{num} x 10 = {int(num)*10}")

#Ejercicio 7

print(" ")
print("--------------------------------------")

num1=int(input("dime el primer numero (disntinto de 0): "))
num2=int(input("dime el segundo numero (disntinto de 0): "))

suma=num1+num2
resta=num1-num2
multi=num1*num2
division=num1/num2

if num1==0 or num2==0:
    print("los numeros no pueden ser 0")
else:
    print(" ")
    print(f"la suma de los numeros es de {suma}")
    print(f"la resta de los numeros es de {resta}")
    print(f"la multiplicacion de los numeros es de {multi}")
    print(f"la division de los numero es de {division}")
    
#Ejercicio 8

print(" ")
print("--------------------------------------")

altura=float(input("dime tu altura en metros: "))
peso=(input("dime tu peso en kg: "))
imc=float(peso)/(altura**2)

print(f"tu indice de masa corporal es de {imc}")

#Ejercicio 9

print(" ")
print("--------------------------------------")

celsius=input("dime la temperatura en grados celsius:")
fahren=(float(celsius)*9/5)+32

print(f"el equivalente en grados fahrenheit es {fahren}")

#Ejercicio 10

print(" ")
print("--------------------------------------")

num1=int(input("dime el primer numero: "))
num2=int(input("dime el segundo numero: "))
num3=int(input("dime el tercer numero: "))

promedio=(num1+num2+num3)/3

print(f"el promedio de los tres numeros ingresados es de {promedio}")