from collections import deque
import time 
cola = deque()
activo = true 
while activo != false:
    match eleccion: 
    print("""
    1. Encolar Elementos
    2. Desencolar Elementos 
    3. Vaciar Cola
    4. Salir
    """)
    eleccion =int(input('Ingresa una eleccion a ejecutar: '))
    case 1: 
        datos = int(input('Ingresa el numero de elementos: '))
        for n in datos: 
            cola.append('Elemento'+str(n))
            print(cola[n])
    case 2:
        datos = int(input('Ingresa el numero de datos a desencolar: '))
        if len(cola)==0:
            print('No existen datos en la cola')
        else: 
            for n in datos: 
                datos_anterior = cola.popleft()
                print
                if len(cola)==0:
                    print('Te has agotado los elementos de la cola :v')
                    break
    case 3: 
        while cola: 
            datos_anterior = cola.popleft()