def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    intersection_len = len(set(recommended[:k]) & set(relevant))

    precision_k = intersection_len/k
    recall_k = intersection_len/len(relevant)

    return [precision_k,recall_k]