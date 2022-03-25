# Calcular el promedio de 3 calificaciones

# Entrada de datos

calificación1 = float(input("Dame la calificacion 1 : "))
calificación2 = float(input("Dame la calificacion 2 : "))
calificación3 = float(input("Dame la calificacion 3 : "))

 # proceso
Calificaciones = (calificación1 + calificación2 + calificación3)/3
if (Calificaciones >= 6): 
    print("Aprobado")
elif(Calificaciones < 6):
    print("Reprobado")

print(f"El promedio de calificaciones es = {Calificaciones}")

