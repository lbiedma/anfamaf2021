def ilagrange(x, y, z):
    if len(x) != len(y):
        print("X e Y no tienen la misma longitud, chau")
        return None

    n = len(x)
    w = []

    for z_i in z:
        # sumatoria de los polinomios base l_i por y_i
        w_i = 0.0
        for idx in range(n):
            # productoria para generar el polinomio base l_i evaluado en z_i
            l_i = 1.0
            for jdx in range(n):
                if jdx != idx:
                    l_i = l_i * (z_i - x[jdx]) / (x[idx] - x[jdx])

            w_i = w_i + y[idx] * l_i

        w.append(w_i)

    return w
