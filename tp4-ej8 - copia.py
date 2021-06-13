################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_primo(numero):
    contador_primo=0
    for i in range(1,1000):
        if numero / i == 1 or numero / i == numero:
            contador_primo=contador_primo+1
        else:
            pass
    if contador_primo==2:
        return True
    else:
        return False

        
def prueba():
    saludo="Números primos "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    numero=int(input("Ingrese un número: "))
    resultado=es_primo(numero)
    if resultado is True:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")
if __name__ == "__main__":
    prueba()