def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")



def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

def mostrar_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci(i)}")


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    binario = decimal_a_binario(n)
    return binario if binario else "0"



def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)



def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)



def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

#---------------------------------------------------------

# Principal

print("Factorial:\n")
try:
    numero = int(input("Ingrese un numero: "))
    if numero < 1:
        print("Debe ser mayor a 0.")
    else:
        mostrar_factoriales(numero)
except ValueError:
    print("Entrada inválida.")

#---------------------------------------------------------

print("\nFibonacci:\n")
try:
    numero_1 = int(input("Ingrese un numero: "))
    if numero_1 < 0:
        print("Debe ser un número positivo.")
    else:
        mostrar_fibonacci(numero_1)
except ValueError:
    print("Entrada inválida.")

#---------------------------------------------------------

print("\n Potencia:\n")
try:
    base = int(input("Ingrese la base: "))
    expo = int(input("Ingrese la potencia: "))
    print(f"{base}^{expo} = {potencia(base, expo)}")
except ValueError:
    print("Entrada inválida.")

#---------------------------------------------------------

print("\n Binario:\n")
try:
    numero_2 = int(input("Ingrese un numero: "))
    if numero_2 < 0:
        print("Debe ser positivo.")
    else:
        print(f"Binario de {numero_2} = {convertir_a_binario(numero_2)}")
except ValueError:
    print("Entrada inválida.")

#---------------------------------------------------------

print("\n Palindromo:\n")
palabra = input("Ingrese una palabra: ")
if palabra.isalpha():
    print(f"¿'{palabra}' es palíndromo? {es_palindromo(palabra.lower())}")
else:
    print("Solo se permiten letras sin espacios ni símbolos.")

#---------------------------------------------------------

print("\n Digitos:\n")
try:
    digitos = int(input("Ingrese digitos: "))
    if digitos < 0:
        print("Debe ser positivo.")
    else:
        print(f"Suma de dígitos de {digitos} = {suma_digitos(digitos)}")
except ValueError:
    print("Entrada inválida.")

#---------------------------------------------------------

print("\n Bloques:\n")
try:
    Bloques = int(input("Ingrese los bloques de abajo: "))
    if Bloques < 1:
        print("Debe ser al menos 1.")
    else:
        print(f"Total de bloques necesarios: {contar_bloques(Bloques)}")
except ValueError:
    print(" Entrada inválida.")

#---------------------------------------------------------

print("\n Contar digito:\n")
try:
    numero_largo = int(input("Ingrese un numero largo: "))
    numero_buscar = int(input("Ingrese el numero que quiere contar: "))
    if numero_largo < 0 or not (0 <= numero_buscar <= 9):
        print("Verifique que el número sea positivo y el dígito esté entre 0 y 9.")
    else:
        print(f"El dígito {numero_buscar} aparece {contar_digito(numero_largo, numero_buscar)} veces.")
except ValueError:
    print("Entrada inválida.")