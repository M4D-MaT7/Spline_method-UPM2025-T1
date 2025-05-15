import numpy as np 
import matplotlib.pyplot as plt

#Splines grado 3
#S(x) = d + c*(x-x_value) + b*(x-x_value)**2 + a*(x-x_value)**3

def Splines_grado_cubico_natural(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x) - 1
    h = x[1:] - x[:-1]

    if n < 2:
        raise ValueError("Se requieren al menos 3 puntos para aplicar splines cúbicos")

    # Paso 1: Construcción del sistema tridiagonal A·M = B
    A = np.zeros((n-1, n-1))
    B = np.zeros(n-1)

    for i in range(1, n):
        A[i-1, i-1] = 2 * (h[i-1] + h[i])
        if i != 1:
            A[i-1, i-2] = h[i-1]
        if i != n-1:
            A[i-1, i] = h[i]
        B[i-1] = 6 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])

    # Paso 2: Resolver el sistema para la segunda derivada
    M_derivadas = np.linalg.solve(A, B)
    M = np.zeros(n + 1)
    M[1:-1] = M_derivadas


    # Paso 3: Calcular coeficientes
    a = (M[1:] - M[:-1]) / (6 * h)
    b = M[:-1] / 2
    c = (y[1:] - y[:-1]) / h - (2*h*M[:-1] + h*M[1:]) / 6
    d = y[:-1]
    
    def Evaluar_spline_cubico(x):
        x_valor = np.linspace(x[0], x[-1], 100)
        for i in range(len(x) - 1):
            if x[i] <= x_valor <= x[i+1]:
                dx = x_valor - x[i]
                return a[i]*dx**3 + b[i]*dx**2 + c[i]*dx + d[i]
        raise ValueError