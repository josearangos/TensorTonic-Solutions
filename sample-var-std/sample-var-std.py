import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    return {"variance":np.var(x,ddof=1).item(),"standard_deviation":np.std(x,ddof=1).item()}