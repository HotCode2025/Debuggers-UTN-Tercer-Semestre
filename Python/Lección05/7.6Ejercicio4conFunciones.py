# Ejercicio 4: Calculadora de Impuestos
# Crear una funcion para calcular el total de un pago incluyendo
# un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

def calcular_pago_con_impuesto(pago_si_impuesto, impuesto):
    pago_total = pago_si_impuesto + (pago_si_impuesto * impuesto / 100)
    return pago_total

pago = float(input("Ingrese el total sin impuesto: "))
impuesto = float(input("Ingrese el porcentaje del impuesto: "))

pago_con_impuesto = calcular_pago_con_impuesto(pago, impuesto)

print(f"Pago con impuesto: {pago_con_impuesto}")
