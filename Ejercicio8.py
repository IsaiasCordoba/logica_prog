
# Nivel de agua en Cisterna
# Datos de entrada
Nivel_de_agua = float(input("Cual es el Nivel de agua de la Cisterna : "))
# Proceso
if (Nivel_de_agua > 6):
    print(f"Desbordamiento de agua en la Cisterna ")
elif (Nivel_de_agua == 6):
    print(f"Apagar la bomba")
elif (Nivel_de_agua >= 4 <= 6) :
    print(f"Desacelerar la bomba")
elif(Nivel_de_agua >= 2 <= 4):
    print(F"Bomba trabajando")
elif(Nivel_de_agua >= 0 <= 2):
    print(f"Acelerar bomba de agua")
elif(Nivel_de_agua == 0):
    print(f"Encender bomba de agua")
else:print(f"Fuga en Cisterna")


