import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

from Spline_method_1 import Splines_lineal
from Spline_method_2 import Spline_cuadratico
from Spline_method_3 import Splines_grado_cubico_natural

def update_graph(label, ax_graph, function, check_buttons, x_values, f_values):
    
    ax_graph.clear()
    ax_graph.plot(x, function(x), label="Función Real")

    labels = check_buttons.labels # obtiene los textos de todos los botones, generando una lista de etiquetas.
    states = check_buttons.get_status() # obtiene True/False para cada botón indicando si está activado.

    for lbl, active in zip(labels, states): #lbl, active es un objeto de la lista generada por el Zip de labels y states.ip(a, b) en Python empareja los elementos de dos listas (o cualquier iterable) por posición.
        
        if active:

            if lbl.get_text() == "Spline de Grado 1": # Si el botón de Spline de Grado 1 está activado, se graficará la función correspondiente.

                ax_graph.plot(x, Splines_lineal(x_values, f_values), label="Spline de Grado 1")

            elif lbl.get_text() == "Spline de Grado 2": # Si el botón de Spline de Grado 2 está activado, se graficará la función correspondiente.

                ax_graph.plot(x, Spline_cuadratico(x_values, f_values), label="Spline de Grado 2")

            elif lbl.get_text() == "Spline de Grado 3": # Si el botón de Spline de Grado 3 está activado, se graficará la función correspondiente.

                ax_graph.plot(x, Splines_grado_cubico_natural(x_values, f_values), label="Spline de Grado 3")

    ax_graph.legend()

    plt.draw()



def Generate_Spline_GUI(function):

    x_values = np.random.uniform(-10, 10, 7) # Genera 7 puntos aleatorios entre -10 y 10 para la función dada.
    f_values = function(x_values) # Genera 7 puntos aleatorios entre -10 y 10 para la función dada.

    option_list = ["Spline de Grado 1", "Spline de Grado 2", "Spline de Grado 3"]

    fig = plt.figure(figsize=(12, 6))
    grid = fig.add_gridspec(1, 3, width_ratios=[2, 1, 0])

    ax_graph = fig.add_subplot(grid[0, 0])
    x = np.linspace(0, 10, 100)
    ax_graph.plot(x, f_values, label="Función Real")

    ax_side = fig.add_subplot(grid[0, 1])
    ax_side.set_title("Método Spline")
    ax_side.axis('off')

    check_ax = fig.add_axes([0.7, 0.4, 0.15, 0.2])  # [left, bottom, width, height]
    check_buttons = CheckButtons(check_ax, option_list, [False]*len(option_list))

    check_buttons.on_clicked(lambda label: update_graph(label, ax_graph, function, check_buttons, x_values, f_values))

    plt.tight_layout()
    plt.show()