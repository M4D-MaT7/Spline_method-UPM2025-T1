import numpy as np 
import matplotlib.pyplot as plt

def Spline_cuadratico(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x) - 1

    if n < 2:
        raise ValueError("Se requieren al menos 3 puntos para aplicar splines de grado 2")

    h = x[1:] - x[:-1]
    A = np.zeros((2*n, 2*n))
    B = np.zeros(2*n)

    fila = 0
    for i in range(n):
        A[fila, i] = h[i]
        A[fila, n+i] = h[i]**2
        B[fila] = y[i+1] - y[i]
        fila += 1

    for i in range(1, n):
        A[fila, i-1] = 1
        A[fila, n+i-1] = 2*h[i-1]
        A[fila, i] = -1
        B[fila] = 0
        fila += 1

    A[fila, n+0] = 1
    B[fila] = 0

    sol = np.linalg.solve(A, B)
    a = sol[n:]
    b = sol[:n]
    c = y.copy()

    x_spline = []
    y_spline = []
    for i in range(n):
        xi = np.linspace(x[i], x[i+1], 100)
        dx = xi - x[i]
        yi = a[i]*dx**2 + b[i]*dx + c[i]
        x_spline.extend(xi)
        y_spline.extend(yi)

    return np.array(x_spline), np.array(y_spline)