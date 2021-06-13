################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def ordenar_menor_a_mayor(uno, dos, tres):
    list=[]
    list.append(uno)
    list.append(dos)
    list.append(tres)
    list.sort()
    tuple=(list)
    return tuple
def ordenar_mayor_a_menor(uno, dos, tres):
    list=[]
    list.append(uno)
    list.append(dos)
    list.append(tres)
    list.sort()
    list.reverse()
    tuple=(list)
    return tuple

def prueba():
    saludo="Ordenar 3 valores "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    uno=int(input("Ingrese un valor: "))
    dos=int(input("Ingrese un segundo valor: "))
    tres=int(input("¿Serías tan amable de ingresar un tercer valor?: "))
    ordenar_mayor_a_menor(uno, dos, tres)
    ordenar_menor_a_mayor(uno, dos, tres)
    print(f"De menor a mayor es: {ordenar_menor_a_mayor(uno, dos, tres)}")
    print(f"De mayor a menor es: {ordenar_mayor_a_menor(uno, dos, tres)}")
    
if __name__ == "__main__":
    prueba()