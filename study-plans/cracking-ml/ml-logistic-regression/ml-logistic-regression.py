import numpy as np

def logistic_regression(X: list, y: list, lr: float, n_iters: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    X = np.array(X)
    y = np.array(y)

    n_samples, n_features = X.shape 

    w = np.zeros(n_features,dtype=np.float64)
    b = np.float64(0)
    
    for _ in range(n_iters):
        z = X@w+b
        z_clipped = np.clip(z, -500, 500)
        y_hat = 1/(1+np.e**((-1*z_clipped)))
        dw = (X.T@(y_hat - y))/n_samples
        db = np.mean(y_hat - y )
        w = w - lr*dw
        b = b - lr*db
    return w,b