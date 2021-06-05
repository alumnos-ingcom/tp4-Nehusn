################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def prueba():
    saludo="Palíndromo "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    texto=input("Ingrese texto: ")
    es_palindromo(texto)
    
def es_palindromo(texto):
    reverse_txt= texto[::-1]
    if texto==reverse_txt:
        print("True")
    else:
        print("False")
    
if __name__ == "__main__":
    prueba()