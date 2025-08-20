print ("CALCULADORA DE PROPINAS")

total_cuenta=int(input("INGRESA EL MONTO TOTAL DE LA CUENTA: ")

propina1=float(0.10)
propina2=float(0.15)

print("PROPINA SUGERIDA (10%)")

#total de propina sugerida (10%)
propina1_total=total_cuenta*propina1

print(propina1_total)
print("TOTAL A PAGAR")
print(total_cuenta+propina1_total)

print("PROPINA SUGERIDA (20%)")

#total de propina sugerida (20%)
propina2_total=total_cuenta*propina2

print(propina2_total)
print("TOTAL A PAGAR")
print(total_cuenta+propina2_total)
