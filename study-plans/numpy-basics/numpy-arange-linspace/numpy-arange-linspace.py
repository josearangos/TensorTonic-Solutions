import numpy as np

def create_sequence(start: float, stop: float, param: float, kind: str) -> np.ndarray:
    """
    Returns a 1D float64 array containing the requested sequence.
    """
    match kind:
        case "arange":
            return np.arange(start,stop,step=param, dtype=np.float64)
        case "linspace":
            return np.linspace(start,stop,param,dtype=np.float64)