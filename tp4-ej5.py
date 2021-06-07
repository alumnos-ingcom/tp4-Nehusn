################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    if numero < 0:
        print(f"{numero} es negativo")
    elif numero==0:
        print(f"{numero} es cero")
    else:
        print(f"{numero} es positivo")
        
def prueba():
    saludo="Números positivos y negativos"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    numero=int(input("Ingrese un número: "))
    
    signo(numero)
    
if __name__ == "__main__":
    prueba()