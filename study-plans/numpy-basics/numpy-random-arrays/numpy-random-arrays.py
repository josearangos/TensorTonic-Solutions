import numpy as np

def generate_random_array(shape: list, kind: str, seed: int) -> np.ndarray:
    """
    Returns a seeded 2D float64 random array with the requested shape.
    """
    rng = np.random.default_rng(seed = seed)

    if isinstance(shape,list):
        rows, columns = shape
        shape = (rows,columns)
    
    match kind:
        case "uniform":
            return rng.uniform(size=shape)
        case "normal":
            return rng.normal(size=shape)
            

