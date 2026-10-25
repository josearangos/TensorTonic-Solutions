import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    rng = np.random.default_rng(seed=seed)

    x = np.array(x)

    n = len(x)

    means = np.empty((n_bootstrap,))

    alpha = (1-ci)/2

    indexs = rng.integers(0, x.size, size=(n_bootstrap, x.size))

    for i,value in enumerate(indexs):
        bootstrap_i = x[value]
        means[i]=np.mean(bootstrap_i)
    
    lower,upper =  np.percentile(means, [alpha*100, (ci+alpha)*100])
                      
    return {"bootstrap_mean": np.mean(means), "lower": lower.item(), "upper": upper.item()}