import matplotlib.pyplot as plt

from mathtools.dataframe import _get_xyz_df
from mathtools.plot.style import _default_colors, _default_markers

##-\-\-\-\-\-\-\-\-\
## 2-DIMENSION GRAPHS
##-/-/-/-/-/-/-/-/-/

# ------------
# Scatter plot
def _scatter(axis, x, y, data=None, **kwargs):

    # Get the default parameters
    color, kwargs = _default_colors(**kwargs)
    marker, fillstyle, size, kwargs = _default_markers(**kwargs)

    # Get the values from the data frame if needed
    if data is not None:
        x, y = _get_xyz_df(data, x, y)

    # Plot the data
    axis.scatter(x, y, marker=marker, s=size, c=color, **kwargs)
