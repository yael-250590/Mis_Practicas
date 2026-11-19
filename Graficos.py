import matplotlib.python as plt
#1 Lista de fila
datos = [42,12,88,23,7,65,34,50]

#Algoritmo de incersion 
def incersion(arr):
    a=arr.copy()
    comp=0
    for i in range(1, len(a)):
        clave, j = a[i], i - 1
        while j >=0 and a[j] > clave:
            comp += 1
            a[j + 1] = a[j]
            j -= 1
        if j >= 0: comp +=1
        a[j + 1] = clave
    return a, comp

#Algoritmo de Seleccion
def seleccion(arr):
    a = arr.copy
    comp = 0
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if a[j] < a[min_idx]:
                min_idx= j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, comp

# 2. EJECUCION DE AMBOS ALGORITMOS
lista_ordenada, comp_ins = incersion(datos)
_, comp_señ = seleccion(datos)

#3. Graficacion 
fig, (ax1, ax2, ax3)= plt.subplots(1,3, figsize=(12, 3.5))

# 1.- Lista Desordenada 
ax1.bar(range(len(datos)), datos, color='salmon')
ax1.set_title('1. Lista Original')
ax1.set_ylabel('Valor')