def rbisec(fun, I, err, mit):
    """
    Busca el cero de la función fun mediante el método de bisección.
    Entradas:
    - fun: Una función de una variable que devuelva un número
    - I: Una lista que represente un intervalo: [a, b]
    - err: Una tolerancia para considerar una evaluación como cero
    - mit: Cantidad máxima de iteraciones de bisección
    Salidas:
    - hx: Lista de puntos medios visitados
    - hf: Lista de evaluaciones de esso puntos medios
    """

    # Asumimos que I es una lista con al menos 2 numeros
    a = I[0]
    b = I[1]

    # Creamos nuestras listas de salida vacias
    hx = []
    hf = []

    if fun(a) * fun(b) >= 0:
        print("fun(a) y fun(b) tienen el mismo signo o son cero.")
        return hx, hf

    if a >= b:
        print("a no es menor que b, dame un intervalo ordenado.")
        return hx, hf

    for it in range(mit):
        # Calculamos punto medio y evaluamos la funcion ahi
        c = (a + b) / 2
        fun_c = fun(c)

        # Agregamos c y fun(c) a nuestras listas
        hx.append(c)
        hf.append(fun_c)

        # Chequear si estamos en un cero
        if abs(fun_c) < err:
            print("Llegamos a un cero!")
            break

        if fun_c * fun(a) < 0:
            b = c
        else:
            a = c

    return hx, hf


def raiz3(x):
    return x**2 - 3
