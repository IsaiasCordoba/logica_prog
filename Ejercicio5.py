# Pedir la cantidad de grados kelvin y convertirlos a Celsius y Fahrenheit

# datos de entrada
kelvin = float(input("Dame los grados kelvin =  "))


# proceso

# de kelvin a Celsius
Celsius = kelvin - 273.15
# de Kelvin a Fahrenheit
Fahrenheit = ((9 * (kelvin - 273.15))/5) + 32



# salida
print(f"Los grados centigrados son = {Celsius}")
print(f"Los grados fahrenheit son = {Fahrenheit}")