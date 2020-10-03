import numpy as np
import re

##-\-\-\-\-\-\-\-\-\
## PRIVATE FUNCTIONS
##-/-/-/-/-/-/-/-/-/

# ---------------------------------------
# Get a string between single or double quote marks
def _get_quoted_string(text, separator='"'):

    if separator == '"':
        return re.findall(r'"(.*?)"', text, re.DOTALL)[0]
    else:
        return re.findall(r""+separator+"(.*?)"+separator, text, re.DOTALL)[0]

# ---------------------
# Read the xvg metadata
def _read_xvg_metadata(metadata):

    # Dictinary of metadata
    metadata_dict = {}

    # Process all the collected elements
    for line in metadata:

        # Graph title
        if line.split()[0] == 'title':
            metadata_dict['title'] = _get_quoted_string(line)

        # Get the axis label
        elif line.split()[1] == 'label':
            axis = line.split()[0]
            metadata_dict[axis+'_label'] = _get_quoted_string(line)

        # Get the eventual legends
        elif line.split()[1] == 'legend':
            dataline = line.split()[0]
            metadata_dict[dataline+'_legend'] = _get_quoted_string(line).capitalize()

    return metadata_dict

##-\-\-\-\-\-\-\-\
## PUBLIC FUNCTIONS
##-/-/-/-/-/-/-/-/

# ----------------
# Read an xvg file
def read_xvg(file_path, get_metadata=False):

    """Extract data and metadata from a .XVG file generated by GROMACS
    Argument(s):
        file_path {str} -- Relative path to the xvg file of be processed.
        get_metadata {bool} -- (Opt.) Specify whether the metadata should be returned.
                               Default is False.
    Output(s):
        data {np.ndarray} -- Array of data extracted from the xvg file.
        metadata {dict of str} -- Dictionary containing the metadata found in the xvg file.
    """

    # Prepare the containers
    metadata = []
    data = []

    # Open the file
    xvg_toread = open(file_path, 'r')

    # Process all the lines
    for line in xvg_toread:

        # Ignore the header
        if line[0] == "#":
            pass

        # Extract the metadata
        elif line[0] == "@":
            metadata.append(line[1:])

        # Extract the data
        else:
            data.append(line.split())

    # Convert data in a float array
    data = np.array(data).astype(float)

    # Convert the metadata in a dictionary
    metadata = _read_xvg_metadata(metadata)

    if get_metadata:
        return data, metadata
    else:
        return data

# ----------------------------------
# Save several columns as a csv file
def save_cols(file_path, *columns, **kwargs):

    """Save several columns (lists) of data into a single csv file
    Argument(s):
        file_path {str} -- Relative path to the csv file of generate.
        *columns {lists} -- Lists to save in the csv file.
    """

    # Generate the array
    data = np.array([x for x in columns]).T

    # Save the infos
    np.savetxt(file_path, data, **kwargs)
