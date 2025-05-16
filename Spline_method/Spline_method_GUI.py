import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons, Slider
from matplotlib.offsetbox import TextArea, AnnotationBbox

from Spline_method_1 import Splines_lineal
from Spline_method_2 import Spline_cuadratico
from Spline_method_3 import Splines_grado_cubico_natural

def update_graph(label, ax_graph, function, check_buttons, x_eval, data_state):

    x_values = data_state["x_values"]
    f_values = data_state["f_values"]

    ax_graph.clear()
    ax_graph.plot(x_eval, function(x_eval), label="Función Real", color='black')

    labels = check_buttons.labels
    states = check_buttons.get_status()

    for lbl, active in zip(labels, states):

        if active:

            if lbl.get_text() == "Spline de Grado 1":

                x_spline, y_spline = Splines_lineal(x_values, f_values)
                ax_graph.plot(x_spline, y_spline, label="Spline de Grado 1", color='red')

            elif lbl.get_text() == "Spline de Grado 2":

                x_spline, y_spline = Spline_cuadratico(x_values, f_values)
                ax_graph.plot(x_spline, y_spline, label="Spline de Grado 2", color='brown')

            elif lbl.get_text() == "Spline de Grado 3":

                x_spline, y_spline = Splines_grado_cubico_natural(x_values, f_values)
                ax_graph.plot(x_spline, y_spline, label="Spline de Grado 3", color='green')

    ax_graph.scatter(x_values, f_values, color='red', label="Datos")
    ax_graph.legend(loc='lower right')
    plt.draw()

def Generate_Spline_GUI(function):

    initial_n = 1
    x_values = np.random.uniform(-10, 10, initial_n)
    x_values.sort()
    f_values = function(x_values)
    x_eval = np.linspace(-10, 10, 300)

    data_state = {"x_values": x_values, "f_values": f_values}

    option_list = ["Spline de Grado 1", "Spline de Grado 2", "Spline de Grado 3"]
    fig = plt.figure(figsize=(14, 8))
    grid = fig.add_gridspec(2, 3, width_ratios=[2, 1, 0.1], height_ratios=[1, 1])

    ax_graph = fig.add_subplot(grid[:, 0])
    ax_graph.plot(x_eval, function(x_eval), label="Función Real", color='black')
    ax_graph.scatter(x_values, f_values, color='red', label="Datos")

    check_ax = fig.add_axes([0.71, 0.55, 0.2, 0.3])
    check_ax.text(0.45, 1.1, "Método Spline", ha='center', va='bottom', fontsize=20, fontweight='bold', color='black', transform=check_ax.transAxes)
    for spine in check_ax.spines.values():
        spine.set_visible(False)
    check_buttons = CheckButtons(check_ax, option_list, [False]*len(option_list))

    ax_note = fig.add_subplot(grid[1, 1])
    ax_note.set_facecolor((0.5, 0.5, 0.5, 0.3))
    ax_note.set_xticks([])
    ax_note.set_yticks([])

    slider_ax = fig.add_axes([0.715, 0.45, 0.2, 0.03])
    slider = Slider(slider_ax, 'Nº datos', 1, 100, valinit=initial_n, valstep=1, color='red')

    def on_slider_change(val):
        n = int(val)
        x_vals = np.random.uniform(-10, 10, n)
        x_vals.sort()
        f_vals = function(x_vals)
        data_state["x_values"] = x_vals
        data_state["f_values"] = f_vals
        update_graph("", ax_graph, function, check_buttons, x_eval, data_state)

    slider.on_changed(on_slider_change)
    check_buttons.on_clicked(lambda label: update_graph(label, ax_graph, function, check_buttons, x_eval, data_state))

    text_info = (
        "Los métodos de spline son técnicas de interpolación\n"
        "que utilizan funciones polinómicas por tramos para\n"
        "ajustar una curva suave a un conjunto de datos.\n"
        "Permiten evitar oscilaciones no deseadas y asegurar\n"
        "continuidad en la derivada.\n\n"
        "En esta interfaz puedes elegir el tipo de spline\n"
        "con las casillas y modificar el número de puntos\n"
        "con el deslizador. La gráfica se actualiza en\n"
        "tiempo real según tus selecciones."
    )
    textbox = TextArea(text_info, textprops=dict(color='black', fontsize=10))
    floating_box = AnnotationBbox(
        textbox,
        (0.668, 0.44),
        xycoords='figure fraction',
        box_alignment=(0, 1),
        frameon=False
    )
    
    fig.add_artist(floating_box)

    plt.tight_layout()
    plt.show()