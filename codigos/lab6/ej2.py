import numpy as np
from  ejercicio_1 import soltrsup #Aqui importe su soltrsup

#Opción 1 - Calcular los ceros de la matriz
def egauss(A_, b_):

    A = A_.copy()
    b = b_.copy()
    n = A.shape[0]

    for k in range(n-1):
        for i in range(k+1,n):
            if A[k,k] == 0:
                print('El elemento a_kk es igual a cero.')
                return None
            
            m = A[i,k] / A[k,k]

            for j in range(k,n):
                A[i,j] = A[i,j] - m * A[k,j]    
            b[i] = b[i] - m * b[k]

    return A, b

#Opción 2 - Realiza cálculos solo sobre la parte triangular superior.
def egauss(A_, b_):

    A = A_.copy()
    b = b_.copy()
    n = A.shape[0]

    for k in range(n-1):
        for i in range(k+1,n):
            if A[k,k] == 0:
                print('El elemento a_kk es igual a cero.')
                return None
            
            m = A[i,k] / A[k,k]

            for j in range(k+1,n):
                A[i,j] = A[i,j] - m * A[k,j]    
            b[i] = b[i] - m * b[k]

    U = np.triu(A)

    return U, b

def soleg(A,b):
    U, y = egauss(A,b)
    x = soltrsup(U,y)
    return x

'''
A = np.random.rand(4,4)
x = np.random.rand(4)

b = A @ x

x_sol = soleg( A, b )

print(x_sol, x)
'''
