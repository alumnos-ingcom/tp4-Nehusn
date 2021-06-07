################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def minimo(lista):
    for i in range(0, len(lista)):
        minimo=lista[0]
        if minimo<=lista[i]:
            pass
        else:
            minimo=lista[i]
    return minimo

def maximo(lista):
    for i in range(0, len(lista)):
        maximo=lista[0]
        if maximo>=lista[i]:
            pass
        else:
            maximo=lista[i]
    return maximo
    

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
        minimo(lista)
        maximo(lista)
        numero_minimo=minimo(lista)
        numero_maximo=maximo(lista)
        print(f"Minimo es: {numero_minimo}")
        print(f"Máximo es: {numero_maximo}")
        

if __name__ == "__main__":
    prueba()