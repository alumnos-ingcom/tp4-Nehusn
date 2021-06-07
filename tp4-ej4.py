################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara(numero, otro_numero):
    if numero <  otro_numero:
        print("\n-1")
    elif (numero == otro_numero):
        print("\n0")
    else:
        print("\n1")
        
def prueba():
    saludo="Comparación de números"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+ "\n")
    numero=int(input("Ingrese un número: "))
    otro_numero=int(input("Ingrese otro número: "))
    compara(numero, otro_numero)
   
if __name__ == "__main__":
    prueba()