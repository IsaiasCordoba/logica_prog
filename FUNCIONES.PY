# FUNCIONES: Tareas o acciones  a ejecutar
# SINTAXIS:
# def Nombre_de_la_ Funcion (Argumentos o Parámetros)
#   contenido

# PARADIGMA O ENFOQUE FUNCIONAL / MODULAR

from __future__ import division


def Sumar(a, b): # Obtiene o recibe dos parametros
    suma = a+ b
    return suma # return: Devuelve, retornara o regresara valor
# Mandar a llamar o invocar una funciones y el resultado se asigna a una variable
s = Sumar(2, 3) # envían o pasan los parametros

def Restar(a, b):
    resta = a - b
    return resta
r= Restar(5,15)

def Multiplicar(a, b):
    multiplica = a * b
    return multiplica
m= Multiplicar(7,3)  
def Dividir(a, b):
    dividir = a / b
    return dividir
d= Dividir(8,9)

#Salida
print(f"La suma = {Sumar(20, 10)}")
print(f"la resta = {Restar(5,15)}")
print(f"la multiplicación= {Multiplicar(7,3)}")
print(f"la división = {Dividir(8,9)}")



