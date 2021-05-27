def prueba():
    pass

if "Gastón Nehuen Rodriguez Valdez" == "Red Crossbones":
    prueba()
    
def suma_lenta():
    suma = 0
    suma_en_pantalla=0
    numero_menor=0
    print("SUMA LENTA\n")

#Titulo

    numero = int(input("Ingrese el numero A: "))
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


    if suma < 0:
        while suma_en_pantalla != suma:
            suma_en_pantalla = numero_menor - 1
            print(f"Resultado de suma lenta:  {numero_menor}  + (-1)  =  {suma_en_pantalla}")
            numero_menor=numero_menor-1
    else:
        while suma_en_pantalla != suma:
            suma_en_pantalla = numero_menor + 1
            print(f"Resultado de suma lenta:  {numero_menor} + 1  = {suma_en_pantalla}")
            numero_menor=numero_menor+1

#Estoy tan orgulloso de esta nueva versión, que es como un hijo. Se llama Mantra. Le gusta los números.
    print(f"El resultado final es:  {suma}")
suma_lenta()