################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def prueba():
    pass

if __name__ == "__main__":
    prueba()

def suma_lenta():
    suma = 0
    suma_en_pantalla=0
    numero_menor=0
    print("SUMA LENTA\n")

#Titulo
    numero = int(input("Ingrese el numero A: "))
    suma = numero
    otro_numero= int(input("Ingrese el numero B: "))
    suma=numero+otro_numero

#Aca se viene lo jodido
    if numero > otro_numero:
        numero_menor=otro_numero
        print(f"\nEmpezamos desde:  {numero_menor}")
    else:
        numero_menor=numero
        print(f"\nEmpezamos desde:  {numero_menor}")

#Eso no. Esto:
    if suma < 0 and (numero < 0 > otro_numero):
        while suma_en_pantalla != suma:
            suma_en_pantalla = numero_menor - 1
            print(f"{numero_menor} - 1  =  {suma_en_pantalla}")
            numero_menor=numero_menor-1
    elif (numero == 0 or otro_numero == 0):
        print(f" {numero_menor} + {otro_numero}  = {suma_en_pantalla}")
    else:
        while suma_en_pantalla != suma:
            suma_en_pantalla = numero_menor + 1
            print(f"{numero_menor} + 1  = {suma_en_pantalla}")
            numero_menor=numero_menor+1
            
    print(f"El resultado final es:  {suma}")
suma_lenta()
