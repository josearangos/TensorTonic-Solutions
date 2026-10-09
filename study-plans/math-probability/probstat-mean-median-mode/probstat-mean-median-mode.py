import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    val, counts  = np.unique(x,return_counts=True)

    return {"mean":np.mean(x).item(),"median":np.median(x).item(),"mode":float(val[counts.argmax()].item())}