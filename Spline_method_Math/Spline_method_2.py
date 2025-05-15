import numpy as np 
import matplotlib.pyplot as plt

#Splines grado 2
#S(x) = c + b*(x-x_value) + a*(x-x_value)**2

def Spline_cuadratico(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x) - 1
    h = x[1:] - x[:-1]

    if n < 2:
        raise ValueError("Se requieren al menos 3 puntos para aplicar splines de grado 2")
    
    # Paso 1: Construir el sistema lineal A * X = B
    A = np.zeros((2*n, 2*n))
    B = np.zeros(2*n)
    fila = 0
    h = x[1:] - x[:-1]

    for i in range(n):
        A[fila, i] = h[i]
        A[fila, n + i] = h[i]**2
        B[fila] = y[i+1] - y[i]
        fila += 1

    for i in range(1, n):
        A[fila, i-1] = 1
        A[fila, n + i-1] = 2 * h[i-1]
        A[fila, i] = -1
        B[fila] = 0
        fila += 1

    A[fila, n + 0] = 1
    B[fila] = 0

    # Paso 2: Resolver el sistema
    sol = np.linalg.solve(A, B)
    a = sol[n:]
    b = sol[:n]
    c = y.copy()

    def Evaluar_spline_cuadratico(x):
        x_valor = np.linspace(x[0], x[-1], 100)
        for i in range(len(x) - 1):
            if x[i] <= x_valor <= x[i+1]:
                dx = x_valor - x[i]
                return a[i]*dx**2 + b[i]*dx + c[i]
        raise ValueError