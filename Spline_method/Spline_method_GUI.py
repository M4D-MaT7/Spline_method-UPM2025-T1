import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

from Spline_method_1 import Splines_lineal
from Spline_method_2 import Spline_cuadratico
from Spline_method_3 import Splines_grado_cubico_natural

def update_graph(label, ax_graph, function, check_buttons, x_eval, x_values, f_values):
    ax_graph.clear()
    ax_graph.plot(x_eval, function(x_eval), label="Función Real", color='black')

    labels = check_buttons.labels
    states = check_buttons.get_status()

    for lbl, active in zip(labels, states):
        if active:
            if lbl.get_text() == "Spline de Grado 1":
                x_spline, y_spline = Splines_lineal(x_values, f_values)
                ax_graph.plot(x_spline, y_spline, label="Spline de Grado 1")
            elif lbl.get_text() == "Spline de Grado 2":
                x_spline, y_spline = Spline_cuadratico(x_values, f_values)
                ax_graph.plot(x_spline, y_spline, label="Spline de Grado 2")
            elif lbl.get_text() == "Spline de Grado 3":
                x_spline, y_spline = Splines_grado_cubico_natural(x_values, f_values)
                ax_graph.plot(x_spline, y_spline, label="Spline de Grado 3")

    ax_graph.scatter(x_values, f_values, color='red', label="Datos")
    ax_graph.legend()
    plt.draw()

def Generate_Spline_GUI(function):
    x_values = np.random.uniform(-10, 10, 50)
    x_values.sort()
    f_values = function(x_values)

    x_eval = np.linspace(x_values[0], x_values[-1], 300)

    option_list = ["Spline de Grado 1", "Spline de Grado 2", "Spline de Grado 3"]

    fig = plt.figure(figsize=(14, 8))
    grid = fig.add_gridspec(2, 3, width_ratios=[2, 1, 0.1], height_ratios=[1, 1])

    # Gráfico principal
    ax_graph = fig.add_subplot(grid[:, 0])
    ax_graph.plot(x_eval, function(x_eval), label="Función Real", color='black')
    ax_graph.scatter(x_values, f_values, color='red', label="Datos")

    # Panel superior derecho (CheckButtons)
    ax_side_top = fig.add_subplot(grid[0, 1])
    ax_side_top.set_title("Método Spline")
    ax_side_top.axis('off')

    check_ax = fig.add_axes([0.72, 0.55, 0.2, 0.3])
    for spine in check_ax.spines.values():
       spine.set_visible(False)
    check_buttons = CheckButtons(check_ax, option_list, [False]*len(option_list))

    check_buttons.on_clicked(lambda label: update_graph(label, ax_graph, function, check_buttons, x_eval, x_values, f_values))

    plt.tight_layout()
    plt.show()