import matplotlib.pyplot as plt

from mathtools.common import _get_kwarg

from mathtools.plot.graph2d import _scatter
from mathtools.plot.style import _set_label

##-\-\-\-\-\-\
## GRAPH CLASS
##-/-/-/-/-/-/

class Graph:
    def __init__(self, **kwargs):

        # Get the subplot shape
        subplots_shape, kwargs = _get_kwarg(kwargs, 'subplots', (1,1), delete=True)

        # Initialise the figure
        self.figure = plt.figure(**kwargs)

        # Populate the axes
        self.axes = []
        for i in range(subplots_shape[0]*subplots_shape[1]):
            self.axes.append( SubGraph(self.figure, subplots_shape[0], subplots_shape[1], i+1) )

        # Remove the list if only one axes is available
        if len(self.axes) == 1:
            self.axes = self.axes[0]

    ##-\-\-\-\-\-\-\-\-\
    ## PRIVATE FUNCTIONS
    ##-/-/-/-/-/-/-/-/-/

    # ---------------
    # Select the axis
    def _select_axis(self, axis=0):

        # Selection
        if isinstance(self.axes, list):
            current_axis = self.axes[axis]
        else:
            current_axis = self.axes

        return current_axis

    ##-\-\-\-\-\-\-\-\-\-\-\-\
    ## DISPLAY DATA IN A GRAPH
    ##-/-/-/-/-/-/-/-/-/-/-/-/

    # -------------------------------
    # Plot the data in a scatter plot
    def scatter(self, x, y, axis=0, **kwargs):
        current_axis= self._select_axis(axis=axis)
        current_axis.scatter(x, y, **kwargs)

    ##-\-\-\-\-\-\-\-\
    ## ADD INFORMATION
    ##-/-/-/-/-/-/-/-/

    # ----------------------------
    # Set the x label for the axis
    def xlabel(self, text, axis=0, **kwargs):
        current_axis= self._select_axis(axis=axis)
        current_axis.xlabel(text, **kwargs)

    # ----------------------------
    # Set the y label for the axis
    def ylabel(self, text, axis=0, **kwargs):
        current_axis= self._select_axis(axis=axis)
        current_axis.ylabel(text, **kwargs)

    ##-\-\-\-\-\-\-\-\
    ## SHOW THE FIGURE
    ##-/-/-/-/-/-/-/-/

    # ---------------
    # Save the figure
    def savefig(self, path, tight_layout=True, **kwargs):

        # Tighten the figure
        if tight_layout:
            plt.tight_layout()

        # Display the figure
        plt.savefig(path, **kwargs)

    # ------------------
    # Display the figure
    def show(self, tight_layout=True):

        # Tighten the figure
        if tight_layout:
            plt.tight_layout()

        # Display the figure
        plt.show()

##-\-\-\-\-\-\-\
## SUBGRAPH CLASS
##-/-/-/-/-/-/-/

class SubGraph:
    def __init__(self, figure, nrows, ncols, id):

        # Get the axis definition
        self.n_rows, self.n_cols = nrows, ncols
        self.index = id

        # Define the axis
        self.axis = figure.add_subplot(nrows, ncols, id)

    ##-\-\-\-\-\-\-\-\-\-\-\-\
    ## DISPLAY DATA IN A GRAPH
    ##-/-/-/-/-/-/-/-/-/-/-/-/

    # -------------------------------
    # Plot the data in a scatter plot
    def scatter(self, x, y, **kwargs):
        _scatter(self.axis, x, y, **kwargs)

    ##-\-\-\-\-\-\-\-\
    ## ADD INFORMATION
    ##-/-/-/-/-/-/-/-/

    # ----------------------------
    # Set the x label for the axis
    def xlabel(self, text, **kwargs):
        _set_label(self.axis, text, side='x', **kwargs)

    # ----------------------------
    # Set the y label for the axis
    def ylabel(self, text, **kwargs):
        _set_label(self.axis, text, side='y', **kwargs)
