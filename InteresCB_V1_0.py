#INICIO

print("Dato saldo actual: ")
Saldo = float(input())

#Empieza la condición

if(Saldo < 10000.00):
    Saldo = Saldo * (1 + 0.03)
else:
    Saldo = Saldo * (1 + 0.04)
#Fin del if
print("Saldo final es %5.2f"%Saldo)

#FIN