# Ejercicio 6 
import math

 # datos de entrada
valor_a = float(input("El valor de a =  "))
valor_b = float(input("El valor de b =  "))
valor_c = float(input("El valor de c =  "))
# proceso 
x1 = (- valor_b - pow((valor_b ** 2) - (4 * valor_a * valor_c), 1/2))/2 * valor_a
x2 = (- valor_b + pow((valor_b ** 2) - (4 * valor_a * valor_c), 1/2))/2 * valor_a

# salida
print(f"El valor de X1 es = {x1}")
print(f"El valor de X2 es = {x2}")

