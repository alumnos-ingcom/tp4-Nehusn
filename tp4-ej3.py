################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def prueba():
    print("CONVERTOR DE GRADOS")

def convertir_a_fahrenheit(centigrados):
    fahrenheit= (centigrados * 9/5) + 32
    print(f"Farenheit: {fahrenheit}°")

def convertir_a_centigrados(fahrenheit):
    centigrados= (fahrenheit - 32) * 5/9
    print(f"Centigrados: {centigrados}°")
    
if __name__ == "__main__":
    prueba()
