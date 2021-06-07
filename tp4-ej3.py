################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
    
def convertir_a_fahrenheit(centigrados):
    fahrenheit= (centigrados * 9/5) + 32
    return fahrenheit

def convertir_a_centigrados(fahrenheit):
    centigrados= (fahrenheit - 32) * 5/9
    return centigrados
    
def prueba():
    saludo="Conversión de temperaturas"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+ "\n")
###################################################################
    
    centigrados=float(input("Ingrese el grado fahrenheit: "))
    fahrenheit=float(input("Ingrese grado centigrado: "))
    convertir_a_centigrados(fahrenheit)
    convertir_a_fahrenheit(centigrados)
    exit_1=convertir_a_centigrados(fahrenheit)
    exit_2=convertir_a_fahrenheit(centigrados)
    print(f"Centigrados: {exit_1}°")
    print(f"Farenheit: {exit_2}°")
    
if __name__ == "__main__":
    prueba()