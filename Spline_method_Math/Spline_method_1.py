import numpy as np 
import matplotlib.pyplot as plt

#Splines grado 1
# S(x) = ax + b

def Splines_lineal(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x) - 1
    a = np.zeros(n)
    b = np.zeros(n)

    if n < 1:
        raise ValueError("Se requieren al menos 2 puntos para aplicar splines de grado 2")

    for i in range(n):
        a[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])
        b[i] = y[i] - a[i] * y[i]

    def Evaluar_spline_lineal(x):
        x_valor = np.linspace(x[0], x[-1], 100)
        for i in range(len(x) - 1):
            if x[i] <= x_valor <= x[i+1]:
                return a[i]*x_valor + b[i]
        raise ValueError