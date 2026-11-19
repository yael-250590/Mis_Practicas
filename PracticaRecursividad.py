def ordenLista(publicaciones: list) -> list:
    if len(publicaciones)<=1:
        return publicaciones

    if publicaciones[0] == publicaciones [1]:
        return ordenLista(publicaciones[1:])
    else :
        return [publicaciones[0]]+ ordenLista(publicaciones[1:])
lista=["Post A", "Post B", "Post B" ,"Post C", "Post B"]
print(ordenLista(lista))

def calcular_saldo_final(listaDeposito: list, interes : float):
    if len(listaDeposito) ==0:
        return 0+listaDeposito[0]*interes
