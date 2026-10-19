platos=[]
activado = True
while activado !=False:
    print("""
        1. Apilar Elementos
        2. Consultar el Elemento Top
        3. Desapilar Elementos
        4. Consultar Tamaño o si esta vacia
        5. Vaciar por completo la pila
        6. Salir
        """)
    eleccion = int(input('Ingresa que Eleccion deseas ejecutar: '))
    match eleccion:
        case 1:
            elementosApilar = int(input('Ingresa cuantos elementos deseas apilar: '))
            for i in range (elementosApilar):
                platos.append("Plato: " + str(i+1))
        case 2:
            if len(platos)==0:
                print("No existen platos")
            else:
                tope = platos[-1]
                print("El tope de la pila es: ", tope)
        case 3:
            elementosQuitar = int(input("¿Cuántos platos deseas desapilar?: "))
            
            for i in range(elementosQuitar):
                
                if platos: 
                    plato_sacado = platos.pop()
                    print(f"Se desapiló: {plato_sacado}")
                else:
                    print("¡Ya no quedan más platos por desapilar!")
                    break
        case 4:
            if len(platos)==0:
                print('Esta vacia la pila')
            else:
                print("La pila tiene " +str(len(platos)) + " elementos")
        case 5:
            if len(platos) ==0: 
                print("Ya no queda ningun plato!")
            else:
                while len(platos) !=0 :
                    plato_sacado = platos.pop()
                    print(f"Se quito {plato_sacado}")                    
                print("Se han quitado todos los platos")                           
        case 6:
            print("Saliendo....")
            activado=False
        case _:
            print('Eleccion Invalida')