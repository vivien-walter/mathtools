import numpy as np
from scipy.interpolate import interp1d

##-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
## INITIALIZE THE FIT PARAMETERS
##-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

# --------------------------------------
# Initialise the parameters for the line
def _initialise_linear(x, y):

    # First point
    x_1, y_1 = np.amin(x), np.amin(y)

    # Second point
    x_2, y_2 = np.amax(x), np.amax(y)

    # Parameters
    a = (y_2 - y_1) / (x_2 - x_1)
    b = y_2 - a * x_2

    return a, b

# -----------------------------------------
# Initialise the parameters for the sigmoid
def _initialise_sigmoid(x, y):

    # Initalise the plateaux
    a1, a2 = np.amin(y), np.amax(y)

    # Interpolate the data
    interpolation_function = interp1d(x, y)
    inter_x = np.arange(np.amin(x), np.amax(x), (np.amax(x)-np.amin(x))/100)
    inter_y = interpolation_function(inter_x)

    # Find the center
    mid_value = (a1 + a2)/2
    xc = inter_x[np.argmin(abs(inter_y - mid_value))]

    # Guess the slope
    dx = 1

    return a1, a2, xc, dx
