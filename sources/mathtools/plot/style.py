import matplotlib.pyplot as plt

from mathtools.common import _get_kwarg, _replace_kwarg

##-\-\-\-\-\-\-\-\
## GRAPH PROPERTIES
##-/-/-/-/-/-/-/-/

# -------------------
# Get multiple kwargs
def _get_multi_kwarg(default, key1, *other_keys, **kwargs):

    # Create the key and value lists
    other_keys=list(other_keys)
    other_keys.append(key1)
    all_values = []
    for key in other_keys:
        crt_value, kwargs = _get_kwarg(kwargs, key, None, delete=True)
        all_values.append(crt_value)

    # Set default if everything is None
    n_none = sum(x is None for x in all_values)
    if n_none == len(all_values):
        value = default

    # Get the main key if more than one not None
    elif n_none <= len(all_values) - 2:
        value = [x for x in all_values if x is not None][-1]

    # Get the not None value
    else:
        value = [x for x in all_values if x is not None][0]

    return value, kwargs

# ---------------------------
# Default colors and settings
def _default_colors(from_dict=True, **kwargs):

    """
    Default plot color:
    - Black ('k')
    - See dictionary for color codes
    """
    # Set the default
    default_color = 'black'

    # Color dictionary
    color_dict = {
    'black':'k',
    'red':'r',
    'blue':'b'
    }

    # Get the value from the kwarg
    color, kwargs = _get_multi_kwarg(default_color, 'color', 'c', **kwargs)

    # Get the color from the dictionary
    if from_dict and color in color_dict.keys():
        color = color_dict[color]

    return color, kwargs

# ------------------------
# Default size for scatter
def _default_markers(**kwargs):

    """
    Default marker properties:
    - Style: round ('o')
    - Fillstyle: full
    - Size: 80
    """
    # Set the default
    marker_style = 'o'
    marker_fs = 'full'
    marker_size = 80

    # Get the value from the kwarg
    marker_style, kwargs = _get_kwarg(kwargs, 'marker', marker_style, delete=True)
    marker_fs, kwargs = _get_kwarg(kwargs, 'fillstyle', marker_fs, delete=True)
    marker_size, kwargs = _get_multi_kwarg(80, 'size', marker_size, **kwargs)

    return marker_style, marker_fs, marker_size, kwargs

##-\-\-\-\-\-\-\-\-\-\-\
## DESIGN OF THE ELEMENTS
##-/-/-/-/-/-/-/-/-/-/-/

# ----------------------------------------
# Get the default properties for the label
def _default_label_properties(**kwargs):

    # Set fontweight
    kwargs = _replace_kwarg(kwargs, 'fontweight', 'bold', keep=True)

    # Set font size
    kwargs = _replace_kwarg(kwargs, 'fontsize', 18, keep=True)

    return kwargs

# ----------------------------------------------
# Set the properties of the X label of the graph
def _set_label(axis, text, side='x', **kwargs):

    # Load the properties in the kwargs
    kwargs = _default_label_properties(**kwargs)

    # Set the label
    if side == 'x':
        axis.set_xlabel(text, **kwargs)
    elif side == 'y':
        axis.set_ylabel(text, **kwargs)
