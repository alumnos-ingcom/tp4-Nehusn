################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def prueba():
    saludo="Restas sucesivas "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    dividendo=int(input("Ingrese el dividendo: "))
    divisor=int(input("Ingrese el divisor: "))
    division_lenta(dividendo, divisor)

#Funcion   
def division_lenta(dividendo, divisor):
    resto=dividendo
    cociente=0
    cociente_decimal=0
    activo=True
    decimal=False
    negativo=False
    
    #Numeros negativos
    if dividendo and divisor < 0:
        negativo=True
        resto=resto * (-1)
        divisor=divisor * (-1)
    elif (dividendo or divisor) < 0:
        if dividendo < 0:
            resto= resto * (-1)
            negativo=True
    elif divisor < 0:
        divisor= divisor * (-1)
        negativo=True
    else:
        negativo=False
        
#Calculos    
    while activo==True:
        #Si el dividendo es menor al divisor
        if (decimal==False) and (resto<divisor) and (resto !=0) and (cociente == 0):
            cociente_decimal=cociente
            resto=resto*10
            cociente=0
            decimal=True
        elif (decimal==False) and (resto<divisor) and (resto !=0) and (cociente != 0):
            cociente_decimal=cociente
            resto=resto*10
            cociente=0
            decimal=True
        #Division comun
        elif resto >=divisor:
            resto=resto-divisor
            cociente=cociente + 1
            
        #Final de programa
        else:
            activo=False

#Imprimir resultados
    if decimal==False and negativo==False:
        print(f"\nEl cociente es: {cociente}")
        print(f"El resto es: {resto}")
    elif (decimal == True) and (negativo==False):
        print(f"\nEl cociente es: {cociente_decimal},{cociente}")
        print(f"El resto es: {resto}")
    elif (decimal==False) and (negativo==True):
        print(f"\nEl cociente es: -{cociente}")
        print(f"El resto es: {resto}")
    elif (decimal==True) and (negativo==True):
        print(f"\nEl cociente es: -{cociente_decimal},{cociente}")
        print(f"El resto es: {resto}")
        
            
if __name__ == "__main__":
    prueba()