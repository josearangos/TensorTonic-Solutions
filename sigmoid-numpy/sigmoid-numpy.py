import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    x = np.array(x)
    deno = (np.e)**(-1*x)
    return 1/(1+deno)