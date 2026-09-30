import calendar
import datetime
import random
def calcular_area_cuadrado(lado):
    area=lado*lado
    print(f"El area del cuadrado es: {area}")
calcular_area_cuadrado(10)

def adivinar_el_numero(numIngresado):
    numeroEntero=random.randint(1,10)
    if (numIngresado==numeroEntero):
        print(f"Felicidades has adivinado el numero {numIngresado}")
    else:
        print(f"El numero era: {numeroEntero} ¡Suerte para la Proxima!")
adivinar_el_numero(5)

def numero_Aleatorio():
    numeroAleatorio=random.randint(1,1000)
    print(f"El numero aleatorio generado es: {numeroAleatorio}")
numero_Aleatorio()

def calendario ():
    anio_actual = datetime.datetime.now().year
    es_bisiesto = calendar.isleap(anio_actual)
    print(f"¿El año {anio_actual} es bisiesto?: {es_bisiesto}")
calendario()

def saludar():
    print("Hola,Bienvenid@s")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es:{hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado=calcular_area_triangulo(10,5)
print(f"El área del triángulo es:{resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre},tienes {edad} años")
saludar_persona("Raul",19)