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

# esta funcion imprime los datos de un arreglo
def imprimir_datos(datos):
    print("")
    print("---------------------------------------------------------")
    for dato in datos:
        print(dato)
    print("---------------------------------------------------------")