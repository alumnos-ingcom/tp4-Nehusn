################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def prueba():
    saludo="Números primos "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    numero=int(input("Ingrese un número: "))
    es_primo(numero)
def es_primo(numero):
    primos=[2,3,5,7,11]
    primo=False
    divisible_por_dos=False
    divisible_por_tres=False
    divisible_por_siete=False
    divisible_por_once=False
#Si numero esta dentro de la cadena de primos   
    if numero in primos:
        primo=True
    else:
        primo=False
#Si numero es divisble por 2       
    if numero % 2 != 0:
        divisible_por_dos=False
    else:
        divisible_por_dos=True
#Si numero es divisble por 3  
    if numero % 3 != 0:
        divisible_por_tres=False
    else:
        divisible_por_tres=True
#Si numero es divisble por 5     
    if numero % 5 != 0:
        divisible_por_cinco=False
    else:
        divisible_por_cinco=True
#Si numero es divisble por 7     
    if numero % 7 != 0:
        divisible_por_siete=False
    else:
        divisible_por_siete=True
#Si numero es divisble por 11  
    if numero % 11 != 0:
        divisible_por_once=False
    else:
        divisible_por_once=True
    
    if primo==True:
        print(f"El numero {numero} es primo")
    elif divisible_por_dos==False and divisible_por_tres==False and divisible_por_cinco==False and divisible_por_siete==False and divisible_por_once==False:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")
        
    
if __name__ == "__main__":
    prueba()