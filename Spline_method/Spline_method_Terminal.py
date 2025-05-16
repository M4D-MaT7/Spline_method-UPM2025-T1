import numpy as np
from Spline_method_GUI import Generate_Spline_GUI

def function(x):
    return np.cosh(x)

Generate_Spline_GUI(function)