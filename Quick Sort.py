def quick_sort(lista):
    # Caso base: listas de 0 o 1 elemento ya están ordenadas
    if len(lista) <= 1:
        return lista
    
    # Elegimos el elemento central como pivote
    pivote = lista[len(lista) // 2]
    
    # Dividimos en tres sublistas
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    # Ordenamos recursivamente y unimos
    return quick_sort(menores) + iguales + quick_sort(mayores)


numeros = [34, 7, 23, 32, 5, 62]
ordenada = quick_sort(numeros)
print("Lista ordenada:", ordenada)
