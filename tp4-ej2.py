def prueba():
    pass

if __name__ == "__main__":
    prueba()
    
def suma_lenta():
    falso_numero=1
    cont = 0
    suma = 0
    suma2=0
    numero_menor=0
    print("SUMA LENTA\n")

#Titulo

    numero = int(input("Ingrese el numero A: "))
    suma = numero
    otro_numero= int(input("Ingrese el numero B: "))
    suma=numero+otro_numero

#Aca se viene lo jodido5
    
    if numero > otro_numero:
        numero_menor=otro_numero
        print(f"\nEmpezamos desde:  {numero_menor}")
    else:
        numero_menor=numero
        print(f"\nEmpezamos desde:  {numero_menor}")
    while suma2 != suma:
        if suma < 0:
            if cont < 1:
                cont = cont + 1
                suma2 = numero_menor - 1
                print(f"Resultado de suma lenta: {numero_menor} - {falso_numero}  = " + str(suma2))
                numero_menor=numero_menor-1
            else:
                cont = cont + 1
                resultado=suma2
                suma2 = numero_menor - 1
                print(f"Resultado de suma lenta: {resultado} - {falso_numero}  = " + str(suma2))
                numero_menor=numero_menor-1
        else:
            if cont <=1:
                cont = cont + 1
                suma2 = numero_menor + 1
                print(f"Resultado de suma lenta: {numero_menor} + {falso_numero}  = " + str(suma2))
                numero_menor=numero_menor+1
            else:
                cont = cont + 1
                suma2 = numero_menor + 1
                print(f"Resultado de suma lenta: {numero_menor} + {falso_numero}  = " + str(suma2))
                numero_menor=numero_menor+1
#Me termine mareando igual c:
#Y encima no funciona con numeros negativos
    print(f"El resultado final es:  {suma}")
suma_lenta()