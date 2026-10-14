import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    data = np.array(data, dtype=np.float64)
    match operation:

        case "flatten":  
            return data.flatten()
        case "transpose":
            return data.T
        case "add_batch":
            return np.expand_dims(data,axis=0)

    