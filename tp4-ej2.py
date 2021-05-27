def prueba():
    pass

if __name__ == "__main__":
    prueba()
    
def suma_lenta():
    falso_numero=1
    cont = 0
    suma = 0
    suma2=0
    resultado=0
    print("SUMA LENTA\n")
#Titulo
    numero = int(input("Ingrese el numero A: "))
    suma = numero
    otro_numero= int(input("Ingrese el numero B: "))

    suma=numero+otro_numero
    print(f"\nEmpezamos desde:  {numero}")
#Loop asi no me mareo
    while suma2 < suma:
        if cont < 1:
            cont = cont + 1
            suma2 = suma2 + 1
            print(f"Resultado de suma lenta: {numero} + {falso_numero}  = " + str(suma2))    
        else:
            cont = cont + 1
            resultado=suma2
            suma2 = suma2 + 1
            print(f"Resultado de suma lenta: {resultado} + {falso_numero}  = " + str(suma2))
#Me termine mareando igual c:
#Y encima no funciona con numeros negativos
suma_lenta()