import numpy as np

def create_filled_array(shape: list, kind: str) -> np.ndarray:

    rows,columns = shape

    match kind:
        case "zeros":
            return np.zeros((rows,columns))
        case "ones":
            return np.ones((rows,columns))
