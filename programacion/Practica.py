nombres = []
identificaciones = []

contador = 1

while True:
    print("Ingrese los datos de la persona", contador, "o escriba 'salir' para terminar:")
    nombre = input("Nombre: ")
  
    if nombre.lower() == 'salir':
        break
    
    identificacion = input("Identificación: ")
    nombres.append(nombre)
    identificaciones.append(identificacion)
    
    contador += 1

print("\nMostrando los datos de todas las personas:")
for i in range(len(nombres)):
    print("Persona", i + 1)
    print("Nombre:", nombres[i])
    print("Identificación:", identificaciones[i])