def suma_lenta():
    suma = 0
    suma2=0
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


    if suma < 0:
        while suma2 != suma:
            suma2 = numero_menor - 1
            print(f"Resultado de suma lenta: {numero_menor} - 1  =  {suma2}")
            numero_menor=numero_menor-1
    else:
        while suma2 != suma:
            suma2 = numero_menor + 1
            print(f"Resultado de suma lenta: {numero_menor} + 1  = {suma2}")
            numero_menor=numero_menor+1

#Estoy tan orgulloso de esta nueva versión, que es como un hijo. Se llama Mantra. Le gusta los números.
    print(f"El resultado final es:  {suma}")
suma_lenta()
