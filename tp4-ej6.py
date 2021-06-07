################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def minimo(lista):
    minimo=lista[0]
    print(f"Minimo es: {minimo}")

def maximo(lista):
    lista.reverse()
    maximo=lista[0]
    print(f"Máximo es: {maximo}")

def prueba():
    saludo="Máximo / Mínimo "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    lista=[]
    ingreso=0
    
    while ingreso != "":
        ingreso=input("Ingrese numero: ")
        lista.append(ingreso)
    else:
        lista.pop()
        lista.sort()
        minimo(lista)
        maximo(lista)

if __name__ == "__main__":
    prueba()