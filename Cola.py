from collections import deque
cola = deque()
#Agregar Elementos
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
#SACAR EL PRIMER ELEMENTO ATENDIDO(DESENCOLAR)
atendido=cola.popleft()
#MOSTRAR RESULTADOS
print("Atendido",atendido)
print ("Cola restante",cola)