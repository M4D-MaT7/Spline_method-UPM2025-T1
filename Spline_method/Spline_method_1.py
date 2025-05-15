import numpy as np 
import matplotlib.pyplot as plt

def Splines_lineal(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x) - 1
    a = np.zeros(n)
    b = np.zeros(n)
    for i in range(n):
        a[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])
        b[i] = y[i] - a[i] * x[i]

    x_spline = []
    y_spline = []
    for i in range(n):
        xi = np.linspace(x[i], x[i+1], 100)
        yi = a[i]*xi + b[i]
        x_spline.extend(xi)
        y_spline.extend(yi)

    return np.array(x_spline), np.array(y_spline)