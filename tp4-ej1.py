################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def numero_entre_valores(numero,valorA,valorB):
    numero_mayor=0
    numero_menor=0
    if valorA < valorB:
        numero_mayor=valorB
        numero_menor=valorA
    else:
        numero_mayor=valorA
        numero_menor=valorB
    if numero >= numero_menor and numero <= numero_mayor:
        return True
    else:
        return False
def prueba():
    saludo="Flor "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    valorA=int(input("Ingrese un valor: "))
    valorB=int(input("Ingrese otro valor: "))
    numero=int(input("Ingrese un numero entre esos valores: "))
    numero_entre_valores(numero,valorA,valorB)
    resultado=numero_entre_valores
    print(resultado)
    
if __name__ == "__main__":
    prueba()