import numpy as np

##Opción 1 - Producto Interno
def soltrinf(A,b):

    if np.linalg.det(A) == 0 :
        print('La matriz es singular')
        return None

    n = A.shape[0]
    x = np.zeros(n)

    for i in range(n):
        x[i] = b[i] - np.dot( A[i,:i ], x[:i] )
        x[i] = x[i] / A[i,i]

    return x 

##Opción 2 - Seudocódigo teórico
def soltrinf(A,b):

    if np.linalg.det(A) == 0 :
        print('La matriz es singular')
        return None

    n = A.shape[0]
    x = np.zeros(n)

    for i in range(n):
        suma = 0
        for j in range(i):
            suma  = suma + A[i,j] * x[j]
        x[i] = b[i] - suma
        x[i] = x[i] / A[i,i]

    return x 

'''
A = np.tril(np.random.rand(4,4))
x = np.random.rand(4)

b = A @ x

print(soltrinf(A, b), x)
'''