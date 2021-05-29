################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def prueba():
    saludo="Conversión de temperaturas"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+ "\n")

def convertir_a_fahrenheit(centigrados):
    fahrenheit= (centigrados * 9/5) + 32
    print(f"Farenheit: {fahrenheit}°")

def convertir_a_centigrados(fahrenheit):
    centigrados= (fahrenheit - 32) * 5/9
    print(f"Centigrados: {centigrados}°")
    
if __name__ == "__main__":
    prueba()
