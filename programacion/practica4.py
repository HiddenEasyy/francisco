usuarios = {
    "nombres": [],
    "identificaciones": []
}

while True:
    print("Ingrese los datos de la persona o escriba 's' para finalizar:")
    nombre = input("Nombre: ")

    if nombre == "s" or nombre == "S":
        break

    identificación = input("Identificación: ")

    usuarios["nombres"].append(nombre)
    usuarios["identificaciones"].append(identificación)

for i in range(len(usuarios["nombres"])):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", usuarios["nombres"][i])
    print("Identificación:", usuarios["identificaciones"][i])