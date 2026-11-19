def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        intercambio = False
        # En cada pasada, los últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio de elementos adyacentes
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambio:
            break
    return lista


numeros = [64, 34, 25, 12, 22, 11, 90]
ordenada = ordenamiento_burbuja(numeros)
print("Lista ordenada:", ordenada)
