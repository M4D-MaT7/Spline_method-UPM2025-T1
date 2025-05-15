import numpy as np 
import matplotlib.pyplot as plt

def Splines_grado_cubico_natural(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x) - 1
    h = x[1:] - x[:-1]

    if n < 2:
        raise ValueError("Se requieren al menos 3 puntos para aplicar splines cúbicos")

    A = np.zeros((n-1, n-1))
    B = np.zeros(n-1)

    for i in range(1, n):
        A[i-1, i-1] = 2*(h[i-1]+h[i])
        if i != 1:
            A[i-1, i-2] = h[i-1]
        if i != n-1:
            A[i-1, i] = h[i]
        B[i-1] = 6*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1])

    M_derivadas = np.linalg.solve(A, B)
    M = np.zeros(n+1)
    M[1:-1] = M_derivadas

    a = (M[1:] - M[:-1]) / (6*h)
    b = M[:-1] / 2
    c = (y[1:] - y[:-1])/h - (2*h*M[:-1] + h*M[1:])/6
    d = y[:-1]

    x_spline = []
    y_spline = []
    for i in range(n):
        xi = np.linspace(x[i], x[i+1], 100)
        dx = xi - x[i]
        yi = a[i]*dx**3 + b[i]*dx**2 + c[i]*dx + d[i]
        x_spline.extend(xi)
        y_spline.extend(yi)

    return np.array(x_spline), np.array(y_spline)