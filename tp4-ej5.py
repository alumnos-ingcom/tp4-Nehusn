################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    if numero < 0:
        return "-"
    elif numero==0:
        return 0
    else:
        return "+"
        
def prueba():
    saludo="Números positivos y negativos"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    numero=int(input("Ingrese un número: "))
    
    signo(numero)
    resultado_signo=signo(numero)
    if resultado_signo=="-":
        print(f"{numero} es negativo")
    elif resultado_signo==0:
        print(f"{numero} es cero")
    elif resultado_signo=="+":
        print(f"{numero} es positivo")
        
if __name__ == "__main__":
    prueba()