import numpy as np

def linear_regression_from_scratch(X: list, y: list, lr: float, epochs: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    X = np.array(X)
    y = np.array(y)
    n_features  = len(X[0])
    w=np.zeros(n_features,dtype=np.float64)
    b=np.float64(0)

    for e in range(epochs):
        y_hat = X@w +b
        n = len(y_hat)
        error = y_hat - y
        grad_w = 2 * (X.T @ error) / n
        grad_b = 2 * error.mean()
        w = w - lr*grad_w
        b = b-lr*grad_b

    return w,b
        

    
    
