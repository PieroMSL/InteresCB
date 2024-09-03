class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def calcular_interes(self):
        if self.saldo < 10000:
            tasa_interes = 0.03
        else:
            tasa_interes = 0.04
        self.saldo *= (1 + tasa_interes)