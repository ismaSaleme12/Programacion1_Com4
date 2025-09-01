
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
grupos_cantidad = 2
integrantes_por_grupo = 5
palabra_final = str(" ")

print(" ")
print("CIFRADO CESAR")
corrimiento = int(input("Ingrese el corrimiento: "))

for grupo in range(grupos_cantidad):
    
    print(" ")
    print(f"<GRUPO {grupo + 1}>")
    
    for integrantes in range(integrantes_por_grupo):
        
        print(f"-INTEGRANTE { integrantes + 1}")
        frase = input("-ingrese una frase: ").lower()  
        
        for letra in frase:
            if letra in alfabeto:
            
                indice = alfabeto.index(letra)
                letra_nueva = alfabeto[(indice + corrimiento )% 27]
                palabra_final += letra_nueva

            else:
            
                palabra_final += letra
            
    print(" ")
    print(f"FRASE GRUPO {grupo + 1}: ")
    print(palabra_final)





