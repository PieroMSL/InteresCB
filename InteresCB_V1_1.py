class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def calcular_interes(self):
        if self.saldo < 10000:
            tasa_interes = 0.03
        else:
            tasa_interes = 0.04
        self.saldo *= (1 + tasa_interes)

# Obtener el saldo inicial del usuario
saldo_inicial = float(input("Dato saldo actual: "))

# Crear una instancia de la clase CuentaBancaria
cuenta = CuentaBancaria(saldo_inicial)

# Calcular el interés y actualizar el saldo
cuenta.calcular_interes()

# Imprimir el saldo final
print("Saldo final es: {:.2f}".format(cuenta.saldo))