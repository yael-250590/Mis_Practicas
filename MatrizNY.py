import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
#Suma de elementos
suma = A+B
print("--Suma A+B--")
print(suma)
#MULTIPLICACION DE ELEMENTOS
prod_elem=A+B
print("--Multiplicacion A*B--")
print(prod_elem)
#Producto Matricial
prod_mat=A@B
print(prod_elem)
#Transpuesta
transpuesta =A.T
print("Transpuesta --A")
print(transpuesta)
#Determine e inversa
det=np.linalg.det(A)
inv=np.linalg.inv(B)
print("DETERMINATE DE A")
print(det)
print("INVERSA DE B")
print(inv)

