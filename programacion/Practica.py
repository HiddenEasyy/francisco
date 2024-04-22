usuarios = [[], []]

while True:
    print("Ingrese los datos de la persona o escriba 's' para finalizar:")
    nombre = input("Nombre: ")

    if nombre == "s" or nombre=="S":
        break

    identificación = input("Identificación: ")

    usuarios[0].append(nombre)
    usuarios[1].append(identificación)

for i in range(len(usuarios[0])):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", usuarios[0][i])
    print("Identificación:", usuarios[1][i])