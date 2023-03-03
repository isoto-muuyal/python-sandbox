# esta funcion imprime los datos de un arreglo
def imprimir_datos(datos):
    print("")
    print("---------------------------------------------------------")
    for dato in datos:
        print(dato)
    print("---------------------------------------------------------")

# esta funcion recibe el nombre del estudiante para capturar sus datos
def captura_datos(numero):
    variables = ["nombre", "edad", "numero", "semestre"]
    datos = []
    print("**********************************************************")
    print("Capturar datos persona " + str(numero))
    for variable in variables:
        datos.append(input("cual es tu " + variable + ": "))
    print("**********************************************************")
    return datos

datos1 = captura_datos("A")
datos2 = captura_datos("B")
imprimir_datos(datos1)
imprimir_datos(datos2)

datos_unidos = datos1 + datos2
imprimir_datos(datos_unidos)
print("Union of A and B")
print(datos_unidos)