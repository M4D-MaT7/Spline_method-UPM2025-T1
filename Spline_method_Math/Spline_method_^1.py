import numpy as np 
import matplotlib.pyplot as plt

def f(x):
    return 1/x

#Splines grado 1
# S(x) = ax + b
print("Spline grado 1")

def Splines_grado_1(x_value, f_value):
    n = len(x_value) - 1
    a = np.zeros(n)
    b = np.zeros(n)

    for i in range(n):
        a[i] = (f_value[i+1] - f_value[i]) / (x_value[i+1] - x_value[i])
        b[i] = f_value[i] - a[i] * x_value[i]
    print("a = ",a, "b = ",b)
    return a, b

x_value = np.array ([1,2,4,8])
f_value = np.array ([1,0.5,0.25,0.125])

a,b = Splines_grado_1(x_value, f_value)

def P0(x,a,b):
    return a[0]*x +b[0]
def P1(x,a,b):
    return a[1]*x +b[1]
def P2(x,a,b):
    return a[2]*x +b[2]

# Crear spline y graficar
x_plot  = np.linspace(1,8,100)
x_plot1 = np.linspace(1, 2, 100)
x_plot2 = np.linspace(2, 4, 100)
x_plot3 = np.linspace(4,8,100)

y = f(x_plot)
y1 = P0(x_plot1,a,b)
y2 = P1(x_plot2,a,b)
y3 = P2(x_plot3,a,b)

plt.figure(figsize=(8,5))
plt.plot(x_plot, y, label="f(x) = 1/x", linestyle='--', color="red")
plt.plot (x_plot1, y1, label= "P1(x)= -0.5*x + 1.5 ", color="green")
plt.plot (x_plot2, y2 , label= "P2(x)= -0.125*x + 0.75 ", color="blue")
plt.plot (x_plot3, y3 , label= "P3(x)= -0.03125*x + 0.375 ", color="black")
plt.scatter (x_value, f_value, color = "black")
plt.title("Interpolación por Splines Lineales Grado 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()

print()

#Splines grado 2
#S(x) = c + b*(x-x_value) + a*(x-x_value)**2
print("Spline grado 2")

def Splines_grado_2(x, y,graficar=True):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x) - 1  # Número de intervalos
    print("n =", n)

    if n < 2:
        raise ValueError("Se requieren al menos 3 puntos para aplicar splines de grado 2")
    
    # Paso 1: construir el sistema lineal A * X = B
    A = np.zeros((2*n, 2*n)) #Tenemos en cuenta las n expresiones y las n derivadas
    B = np.zeros(2*n)
    fila = 0
    d = x[1:] - x[:-1]  # distancias de los intervalos
    print("Distancia entre Intervalos =", d)

    # 1. Condiciones de interpolación: S_i(x_{i+1}) = y_{i+1}
    for i in range(n):
        A[fila, i] = d[i]           # coef. de b_i
        A[fila, n + i] = d[i]**2    # coef. de a_i
        B[fila] = y[i+1] - y[i]
        fila += 1

    # 2. Continuidad de derivadas: S_i'(x_{i+1}) = S_{i+1}'(x_{i+1})
    for i in range(1, n):
        A[fila, i-1] = 1                # b_{i-1}
        A[fila, n + i-1] = 2 * d[i-1]   # 2*d*a_{i-1}
        A[fila, i] = -1                # -b_i
        B[fila] = 0
        fila += 1

    # 3. Condición adicional: a_0 = 0  #Tenemos 1 grado de libertad para elegir la última condicion
    A[fila, n + 0] = 1
    B[fila] = 0

    # Paso 2: Resolver el sistema
    print ("A =", A)
    print("B =", B)
    sol = np.linalg.solve(A, B)
    a = sol[n:]
    print ("a =", a)
    b = sol[:n]
    print ("b =", b)
    c = y.copy()  # c_i = y_i directamente
    print("c =", c)

    return a, b, c

x_value = np.array([3,4.5,7,9])
f_value = np.array([2.5,1,2.5,0.5])

a,b,c = Splines_grado_2(x_value,f_value)

def S1(x):
    S1 = c[0] + b[0]*(x - x_value[0]) + a[0]*(x - x_value[0])**2
    return S1

def S2(x):
    S2 = c[1] + b[1]*(x - x_value[1]) + a[1]*(x - x_value[1])**2
    return S2

def S3(x):
    S3 = c[2] + b[2]*(x - x_value[2]) + a[2]*(x - x_value[2])**2
    return S3


# Crear spline y graficar
x_plot1 = np.linspace(3, 4.5, 100)
x_plot2 = np.linspace(4.5, 7, 100)
x_plot3 = np.linspace(7,9,100)

y1 = S1(x_plot1)
y2 = S2(x_plot2)
y3 = S3(x_plot3)

plt.figure(figsize=(8,5))
plt.plot (x_plot1, y1, label= "S1(x)= 2.5 - 1*(x - 3) ", color="green")
plt.plot (x_plot2, y2 , label= "S2(x)= 1 - 1*(x-4.5) + 6.4e-01*(x-4.5)**2 ", color="blue")
plt.plot (x_plot3, y3 , label= "S3(x)= 2.5 + 2.2*(x-7) - 1.6*(x-7)**2", color="black")
plt.scatter (x_value, f_value, color = "black")
plt.title("Interpolación por Splines Lineales Grado 2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()

def Splines_grado_3(x_value, f_value):
    a, b, c = Splines_grado_2(x_value, f_value)
    return a, b, c