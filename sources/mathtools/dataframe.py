import numpy as np
import pandas as pd

##-\-\-\-\-\-\-\-\-\
## PRIVATE FUNCTIONS
##-/-/-/-/-/-/-/-/-/

# ---------------------------------
# Extract columns from a data frame
def _get_xyz_df(data, x, y, z=None):

    # Get the x
    if isinstance(x, str):
        x = data[x]

    # Get the y
    if isinstance(y, str):
        y = data[y]

    # Return a z value if needed
    if z is not None:
        if isinstance(z, str):
            z = data[z]

        return x, y, z

    # Return only x and y
    else:
        return x, y

##-\-\-\-\-\-\-\-\
## PUBLIC FUNCTIONS
##-/-/-/-/-/-/-/-/

# ------------------------------
# Initialise a pandas data frame
def arr2df(input_array, headers=None, constants=None):

    # Calculate the number of columns to create
    if len(input_array.shape) == 1:
        n_cols = 1
    else:
        n_cols = input_array.shape[1]

    # Get the name of the header
    if headers is None:
        headers = [ str(chr(97+i)) for i in range(n_cols) ]

    # Prepare the data dictionary
    data = {}
    if n_cols > 1:
        for i in range(n_cols):
            data[headers[i]] = np.copy(input_array[:,i])
    else:
        data[headers[0]] = np.copy(input_array)

    # Generate the dataframe
    dataframe = pd.DataFrame(data)

    # Add constant values
    if constants is not None:
        for key in constants.keys():
            dataframe[ key ] = [ constants[key] ] * len( dataframe[headers[0]] )

    return dataframe
