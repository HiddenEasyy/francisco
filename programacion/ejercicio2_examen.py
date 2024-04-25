#importamos random
import random
#funcion para general la lista de los random
def generar_lista_aleatoria(n):
    return [random.randint(1, 100) for _ in range(n)]

#Funcion para el diccionario de los cuadrados, tambien se eleva aqui mismo
def crear_diccionario_cuadrados(lista):
    diccionario = {}
    for i, num in enumerate(lista, 1):
        diccionario[i] = num ** 2
    return diccionario

#Funcion que hace todo, pide el digito, imprime las dos listas, 
def main():
    n = int(input("Ingrese el número de elementos en la lista aleatoria: "))
    
    lista_aleatoria = generar_lista_aleatoria(n)
    diccionario_cuadrados = crear_diccionario_cuadrados(lista_aleatoria)
    
    print("Lista de números aleatorios:", lista_aleatoria)
    print("Diccionario de cuadrados de los números aleatorios:")
    for clave, valor in diccionario_cuadrados.items():
        print(clave, ":", valor)

#Ejecuta
if __name__ == "__main__":
    main()