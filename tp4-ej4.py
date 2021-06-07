################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara(numero, otro_numero):
    if numero <  otro_numero:
        retunr -1
    elif (numero == otro_numero):
        return 0
    else:
        return 1
        
def prueba():
    saludo="Comparación de números"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+ "\n")
    numero=int(input("Ingrese un número: "))
    otro_numero=int(input("Ingrese otro número: "))
    compara(numero, otro_numero)
    resultado_compara=compara(numero, otro_numero)
    print(resultado_compara)
    
   
if __name__ == "__main__":
    prueba()