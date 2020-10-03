import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chisquare

from mathtools.fit.preparation_2d import _initialise_linear, _initialise_sigmoid
from mathtools.functions import _get_2D_function

##-\-\-\-\-\
## FIT CLASS
##-/-/-/-/-/

class Fit:

    # -----------------------
    # Initialise the instance
    def __init__(self, mathfunc, x, y, **kwargs):

        # Load the function
        if isinstance(mathfunc, str):
            mathfunc = _get_2D_function(mathfunc)
        self.function = mathfunc

        # Get the data range
        self.x = x
        self.y = y

        # Run the fit
        self.fit(**kwargs)

    ##-\-\-\-\-\-\
    ## CALCULATIONS
    ##-/-/-/-/-/-/

    # ---------------
    # Perform the fit
    def fit(self, **kwargs):

        # Get from the kwargs
        self.yerr = kwargs.get('sigma', kwargs.get('yerr', None))

        # Fit the function
        self.parameters, self.covariances = curve_fit(self.function, self.x, self.y, sigma=self.yerr, **kwargs)

        # Get the error from the covariance matrix
        self.errors = np.sqrt(np.diag(self.covariances))

        # Compute the stats
        self.stats()

        return self.parameters, self.errors

    # -----------------------------------
    # Calculate the statistics on the fit
    def stats(self):

        # Calculate the expected values
        y_exp = self.compute(self.x)

        # Calculate the chi-square
        chi_ddof = self.x.shape[0] - 1 - len(self.parameters)
        self.chi2 = chisquare(self.y, f_exp=y_exp, ddof=chi_ddof)[0]

        return self.chi2

    # -------------------------------
    # Compute values based on the fit
    def compute(self, x):
        return self.function(x, *self.parameters)

    ##-\-\-\-\
    ## DISPLAY
    ##-/-/-/-/

    # --------------------------
    # Show the result of the fit
    def show(self):

        # Plot the fit over the data
        plt.plot(self.x, self.y, 'ko')

        x_fit = np.arange(np.amin(self.x), np.amax(self.x), (np.amax(self.x)-np.amin(self.x))/100)
        plt.plot(x_fit, self.compute(x_fit), 'b--')

        plt.show()

##-\-\-\-\-\-\-\-\-\
## 2-DIMENSIONAL FIT
##-/-/-/-/-/-/-/-/-/

# -----------------------------
# Do a linear fit on the values
def LinearFit(x,y,**kwargs):

    # Initialise the parameters
    if kwargs.get('p0', None) is None:
        kwargs['p0'] = _initialise_linear(x,y)

    return Fit('linear', x, y, **kwargs)

# ------------------------------
# Do a sigmoid fit on the values
def SigmoidFit(x,y,**kwargs):

    # Initialise the parameters
    if kwargs.get('p0', None) is None:
        kwargs['p0'] = _initialise_sigmoid(x,y)

    return Fit('sigmoid', x, y, **kwargs)
