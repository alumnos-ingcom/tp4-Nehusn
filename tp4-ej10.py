################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def factores_primos(numero):
    calculo=0
    global lista
    lista=()
    tupla=()
    contador=1
    while contador < 100:
        calculo=numero*contador
        es_primo(calculo)
        contador=+1
    print(lista)
    
def es_primo(calculo):
    primos=[2,3,5,7,11]
    primo=False
    divisible_por_dos=False
    divisible_por_tres=False
    divisible_por_siete=False
    divisible_por_once=False
#Si numero esta dentro de la cadena de primos   
    if calculo in primos:
        primo=True
    else:
        primo=False
#Si numero es divisble por 2       
    if calculo % 2 != 0:
        divisible_por_dos=False
    else:
        divisible_por_dos=True
#Si numero es divisble por 3  
    if calculo % 3 != 0:
        divisible_por_tres=False
    else:
        divisible_por_tres=True
#Si numero es divisble por 5     
    if calculo % 5 != 0:
        divisible_por_cinco=False
    else:
        divisible_por_cinco=True
#Si numero es divisble por 7     
    if calculo % 7 != 0:
        divisible_por_siete=False
    else:
        divisible_por_siete=True
#Si numero es divisble por 11  
    if calculo % 11 != 0:
        divisible_por_once=False
    else:
        divisible_por_once=True
    
    if primo==True:
        lista=lista.append(calculo)
    elif divisible_por_dos==False and divisible_por_tres==False and divisible_por_cinco==False and divisible_por_siete==False and divisible_por_once==False:
        lista=lista.append(calculo)
    else:
        pass

def prueba():
    saludo="Factores Primos "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    numero=int(input("Ingrese número: "))
    
    factores_primos(numero)
               
if __name__ == "__main__":
    prueba()