def prueba():
    pass

if __name__ == "__main__":
    prueba()
    
def suma_lenta():
    falso_numero=1
    cont = 0
    suma = 0
    resultado=0
    print("SUMA LENTA\n")
#Titulo
    numero = int(input("Ingrese el numero A: "))
    suma = numero
    otro_numero= int(input("Ingrese el numero B: "))
#Loop asi no me mareo
    print(f"Empezamos desde {numero}")
    while suma < otro_numero:
        if cont < 1:
            cont = cont + 1
            suma = suma + 1
            print(f"Resultado de suma lenta: {numero} + {falso_numero}  = " + str(suma))    
        else:
            cont = cont + 1
            resultado=suma
            suma = suma + 1
            print(f"Resultado de suma lenta: {resultado} + {falso_numero}  = " + str(suma))
#Me termine mareando igual
suma_lenta()