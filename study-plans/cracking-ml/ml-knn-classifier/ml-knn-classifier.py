import numpy as np

def knn_classifier(X_train: list, y_train: list, X_test: list, k: int) -> list:
    """
    Returns one predicted label for each test row.
    """
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)

    distances = np.sqrt(np.sum((X_train - X_test[:,np.newaxis,:])**2,axis=2))
    order_indexs = np.argsort(distances,axis=1)
    k_nearst_indexs = order_indexs[:,:k]
    k_nears_pred = y_train[k_nearst_indexs]
    predictions = []
    for row in k_nears_pred:
        values, counts = np.unique(row, return_counts=True)
        mode = values[np.argmax(counts)]
        predictions.append(mode)
    return predictions
