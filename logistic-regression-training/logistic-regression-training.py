import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))
    
def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    y = y.reshape(-1,1)

    n_samples, n_features = X.shape
    b = 0
    w = np.zeros((n_features,1))
    
    for i in range(steps):
        z = X@w+b
        p = _sigmoid(z)

        dw = (1/n_samples)*(X.T@(p-y))
        db = (1/n_samples)*np.sum(p-y)

        w += -lr*dw
        b += -lr*db
    return w.flatten(),b.item()