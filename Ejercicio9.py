# datos de entrada
Sueldo_diario = float(input("Cual es tu sueldo diario =  "))
Mes = input("Que mes quieres calcular =      ")
Días_laborables = int(input("Cuales son tus dias laborables = "))
iva = 0.16
isr = 0.10

# Proceso
iva_trasladado = ((Sueldo_diario * Días_laborables) * iva)
sueldo_bruto = ((Sueldo_diario * Días_laborables) + iva_trasladado) 
sueldo_neto = sueldo_bruto - ((2/3 * iva_trasladado) + (sueldo_bruto *isr))

# datos de salida
print(f"El pago bruto es = {sueldo_bruto}")
print(f"El pago neto es = {sueldo_neto}")
print(f"El mes es = {Mes}")