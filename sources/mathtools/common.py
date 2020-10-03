##-\-\-\-\-\-\-\-\-\-\-\-\-\-\
## KEYWORD ARGUMENT MANAGEMENT
##-/-/-/-/-/-/-/-/-/-/-/-/-/-/

# -----------------------------------------------
# Extract the value from a keyword arguments list
def _get_kwarg(kwargs, key, default, delete=False):

    # Retrieve the value
    value = kwargs.get(key, default)

    # Remove the key if needed
    if delete:
        kwargs.pop(key, None)

    return value, kwargs

# -------------------------------------------------
# Replace an argument in a kwarg by a default value
def _replace_kwarg(kwargs, key, value, keep=True):

    # Keep the value in the kwarg if it exist
    if keep:
        value, _ = _get_kwarg(kwargs, key, value)

    # Replace in the kwarg
    kwargs[key] = value

    return kwargs
