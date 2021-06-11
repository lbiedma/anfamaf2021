import numpy as np

def jacobi(A, b, err, mit):

    n = A.shape[0]
    x = np.zeros(n)
    x_n = np.zeros(n)

    for k in range(mit):
        for i in range(n):
            suma = 0
            for j in range(n):
                if j!=i:
                    suma = suma + A[i,j] * x[j]
            
            x_n[i] = (b[i] - suma)/ A[i,i]

        if np.linalg.norm(x_n - x, np.inf) <= err:
            print('La norma infinito es pequeña')
            return x_n, k+1 
        
        x = x_n.copy() 
        #x_n = np.zeros(n)

    return x, k+1

#A = np.array( [ [10, -1, 2, 0],  [ -1, 11, -1 , 3 ], [ 2, -1, 10, -1], [ 0, 3, -1, 8 ] ] )
#b = np.array([ 6, 25, -11, 15 ])
#print(jacobi( A,b, 1e-6, 100 ))