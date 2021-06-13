################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def saludo(saludo):
    saludo="Palíndromo "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    
def es_palindromo(texto):
    reverse_txt= texto[::-1]
    if texto==reverse_txt:
        return True
    else:
        return False

def prueba():
    saludo(saludo)
    texto=input("Ingrese texto: ")
    resultado=es_palindromo(texto)
    print(resultado)
if __name__ == "__main__":
    prueba()