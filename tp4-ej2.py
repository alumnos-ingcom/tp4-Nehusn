################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def prueba():
    print("SUMA LENTA\n")
    numero = int(input("Ingrese el numero A: "))
    otro_numero= int(input("Ingrese el numero B: "))
    suma_lenta(numero, otro_numero)

def suma_lenta(numero, otro_numero):
    suma_en_pantalla=0
    numero_menor=0
    resultado_suma=numero+otro_numero
#Codigo para elegir un numero menor y empezar a sumar desde ahi

    if numero > otro_numero:
        numero_menor=otro_numero
        print(f"\nEmpezamos desde:  {numero_menor}")
    else:
        numero_menor=numero
        print(f"\nEmpezamos desde:  {numero_menor}")

#Loop para mostar y demostar en pantalla:

#Si es una suma de dos negativos
        
    if resultado_suma < 0 and (numero < 0 > otro_numero):
        while suma_en_pantalla != resultado_suma:
            suma_en_pantalla = numero_menor - 1
            print(f"{numero_menor} + (-1)  =  {suma_en_pantalla}")
            numero_menor=numero_menor-1
            
#Si uno de los numeros o ambos es cero
            
    elif (numero == 0 or otro_numero == 0):
        print(f" {numero_menor} + {otro_numero}  = {suma_en_pantalla}")
        
#Basicamente cualquir otra cosa
        
    else:
        while suma_en_pantalla != resultado_suma:
            suma_en_pantalla = numero_menor + 1
            print(f"{numero_menor} + 1  = {suma_en_pantalla}")
            numero_menor=numero_menor+1

#Para que muestre el resultado final en pantalla
            
    print(f"El resultado final es:  {resultado_suma}")

if __name__ == "__main__":
    prueba()
