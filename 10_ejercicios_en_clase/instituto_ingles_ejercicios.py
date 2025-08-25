print("<EJERCICIO DE PRACTICA>")

print(" ")
print("Observaciones sobre las clases")

#dias validos
dias_validos=["lunes","martes","miercoles","jueves","viernes"]

#fecha de la clase
fecha=input("Ingrese la fecha de la clase (dia, dd/mm): ")
fecha=fecha.split(" ")

dia_semana=fecha[0]
dia_semana=dia_semana.lower()

dd=int(fecha[1])
mm=int(fecha[2])

print(" ")
print(dia_semana,",",dd,"/",mm)

#validacion dias
if dia_semana not in dias_validos:
    print("<EL DIA DE LA SEMANA NO ES VALIDO>")
    exit()

#validacion fechas
if dd<1 or dd>31:
    print("<EL DIA NO ES VALIDO>")
    exit()
elif dd>28 and mm==2 :
    print("<EL DIA NO ES VALIDO>")
    exit()
elif dd>30 and (mm==4 or mm==6 or mm==9 or mm==11):
    print("<EL DIA NO ES VALIDO>")
    exit()


#validacion meses
if mm<1 or mm>12:
    print("<EL MES NO ES VALIDO>")
    exit()
    
    
#EXAMENES
#nivel incial,intermedio y avanzado
if dia_semana=="lunes" or dia_semana=="martes" or dia_semana=="miercoles":
    
    opc=str(input("¿Se tomo examen? (si/no): "))
    opc=opc.lower()
    
    #PORCENTAJE DE APROBADOS
    if opc=="si":
        print(" ")
        print("<APROBADOS EXAMEN>")
        aprobados=int(input("-Ingrese la cantidad de alumnos aprobados: "))
    
        print("<DESAPROBADOS EXAMEN>")
        desaprobados=int(input("-Ingrese la cantidad de alumnos desaprobados: "))

        total_alumnos= aprobados+desaprobados
        porcentaje_aprobados= (aprobados/total_alumnos) *100
    
        print(f"<El porcentaje de alumnos aprobados es:{round(porcentaje_aprobados,2)}%>")
    

#PRACTICA HABLADA
if dia_semana=="jueves":
    
    print(" ")
    print("<ASISTENCIA A PRACTICA HABLADA>")
    porcentaje_asistencia=int(input("-Ingrese el porcentaje de asistencia: "))
    
    if porcentaje_asistencia>50:
        print("<ASISTIO LA MAYORIA>")
    else:
        print("<NO ASISTIO LA MAYORIA>")
        
        
#iINGLES PARA VIAJEROS
if dia_semana=="viernes":
    
    print(" ")
    print("<INGLES PARA VIAJEROS>")
    if dd== 1 and mm== 1 or dd== 1 and mm== 7:
        print("COMIENZO DE NUEVO CICLO")
        
        #cantidad de alumnos 
        cantidad_alumnos=int(input("-Ingrese la cantidad de alumnos nuevos: "))
        arancel_alumnos=int(input("-Ingrese el arancel por alumno: "))
        
        #arancel total
        arancel_total=cantidad_alumnos*arancel_alumnos
        print(f"<EL ARANCEL TOTAL ES: ${arancel_total}>")