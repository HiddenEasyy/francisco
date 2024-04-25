# Definir el diccionario de frutas con nombres y precios
frutas = {
    "manzana": 1.5,
    "banana": 0.75,
    "naranja": 1.0,
    "uva": 2.0,
    "pera": 3.0
}

# Función para calcular el precio total, pero de una fruta nomas, no pide varias al mismo tiempo
def calcular_precio(fruta, cantidad):
    if fruta in frutas:
        precio_unitario = frutas[fruta]
        precio_total = precio_unitario * cantidad
        return precio_total
    else:
        print("Esa fruta no la vendemos chaval JIJI JIJA")

# Función principal del programa para pedir items y cantidades,
# se repite cada que terminas con una fruta y eliges otra
def main():
    while True:
      #try es una funcion que mire, intenta con el try y si no jala (por algun error) se va al otro (except),
      #especial para estos problemas 
        try:
            # Pedir el nombre de la fruta y la cantidad vendida
            fruta = input("Ingrese el nombre de la fruta: ").lower()
            cantidad = int(input("Ingrese la cantidad vendida: "))

            # Calcular el precio final leugo imprimirlo
            precio_final = calcular_precio(fruta, cantidad)
            print(f"El precio final de {cantidad} {fruta}(s) es: {precio_final} pelucholares")
#La sintaxis esta googleada
        except ValueErrosr as e:
            print(e)

        # Preguntar si quiere hacer otra consulta
        continuar = input("¿Desea hacer otra consulta? (s/n): ").lower()
        if continuar != 's':
            break

# ejecutar prog
if __name__ == "__main__":
    main()
