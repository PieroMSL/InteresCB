from InteresCB_V1_1 import CuentaBancaria


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Obtener el saldo inicial del usuario
    saldo_inicial = float(input("Dato saldo actual: "))

    # Crear una instancia de la clase CuentaBancaria
    cuenta = CuentaBancaria(saldo_inicial)

    # Calcular el interés y actualizar el saldo
    cuenta.calcular_interes()

    # Imprimir el saldo final
    print("Saldo final es: {:.2f}".format(cuenta.saldo))

