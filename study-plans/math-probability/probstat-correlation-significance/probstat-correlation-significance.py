import numpy as np
from scipy.stats import t

def correlation_analysis(x: list, y: list) -> dict:
    """
    Returns correlation, explained proportion, test statistic, p-value, and significance.
    """
    x = np.array(x)
    y = np.array(y)

    x = np.array(x)
    y = np.array(y)
        
    pearson_corre = np.corrcoef(x,y)

    correlation_coefficient = pearson_corre[0,1]

    coefficient_of_determination = correlation_coefficient**2

    n = len(x) 

    df = n - 2

    t_statistic = correlation_coefficient * np.sqrt(df) / np.sqrt(1 - coefficient_of_determination)

    p_value = 2 * t.sf(abs(t_statistic), df)

    is_significant = p_value < 0.05

    return {"p_value":p_value.item(),"r":correlation_coefficient.item(),"r_squared":coefficient_of_determination.item(),"significant":is_significant.item(),"t_stat":t_statistic.item()}