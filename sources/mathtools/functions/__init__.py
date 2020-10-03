import numpy as np

##-\-\-\-\-\-\-\-\-\
## PRIVATE FUNCTIONS
##-/-/-/-/-/-/-/-/-/

# -------------------------------------
# Retrieve function from dictionary key
def _get_2D_function(func_name):

    # List all the functions
    func_dict = {
    'linear':linear,
    'proportional': proportional,
    'constant': constant,
    'sigmoid': sigmoid
    }

    return func_dict[func_name]

##-\-\-\-\-\-\-\-\-\-\-\-\
## 2-DIMENSIONAL FUNCTIONS
##-/-/-/-/-/-/-/-/-/-/-/-/

# ---------------
# Linear function
def linear(x, a, b):
    return a*x + b

# ---------------------
# Proportional function
def proportional(x,a):
    return linear(x, a, 0)

# ---------------------
# Proportional function
def constant(x,b):
    return linear(x, 0, b)

# --------------------------
# Boltzmann sigmoid function
def sigmoid(x, a1, a2, xc, dx):
    return (a1-a2) / (1 + np.exp((x-xc)/dx)) + a2
