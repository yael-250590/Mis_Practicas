class Nodo: 
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class listaEnlazada:
    def __init__(self):
        self.cabeza = None #Referencia que indica el origen de la lista
    def insertar_final(self,dato):
        nuevo_nodo=Nodo(dato)

        #Caso 1: si la lista esta vacia el, el nodo se va a convertir en la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        #Caso 2: Recorrer hasta el ultimo elemento o nodo existente
        actual = self.cabeza
        while actual.siguiente is not None:
            actual=actual.siguiente
        actual.siguiente=nuevo_nodo

    def mostrar_lista(self):
        actual= self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual=actual.siguiente
        print("-----".join(elementos)+"..None")

lista=listaEnlazada()

lista.insertar_final("A")
lista.insertar_final("b")
lista.insertar_final("B")

lista.mostrar_lista()
