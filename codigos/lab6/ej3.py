from scipy import linalg

from ej1 import soltrinf, soltrsup

def sollu(A, b):
    # A = P L U
    P, L, U = linalg.lu(A)
    
    # Ax = b -> PLUx = b
    # LUx = P^T b = y
    # Lz = y
    # Ux = z

    y = P.T @ b
    z = soltrinf(L, y)
    x = soltrsup(U, z)

    return x
