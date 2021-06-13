################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def ingreso_entero_reintento():
    while True:
        valor=input("Ingrese un número entero: ")
        try:
            valor=int(valor)
            return valor
        except ValueError as err:
            raise IngresoIncorrecto("No era un número!") from err
######################
def ingreso_entero_restringido(numero,valorA,valorB):
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
    
#######################          
def prueba():
    saludo="Flor "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    valorA=int(input("Ingrese un valor: "))
    valorB=int(input("Ingrese otro valor: "))
    numero=int(input("Ingrese un numero entre esos valores: "))
    
    resultado_restrigido=ingreso_entero_restringido(numero,valorA,valorB)
    resultado_reintento=ingreso_entero_reintento()
    
    ingreso_entero_restringido(numero,valorA,valorB)
    ingreso_entero_reintento()
    
    print(resultado_restrigido)
    print(resultado_reintento)
    
if __name__ == "__main__":
    prueba()