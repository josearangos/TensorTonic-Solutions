def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    relevante_set = set(relevant)

    hits = sum(item in relevante_set for item in recommended[:k])

    precision_k = hits/k if k else 0.0
    recall_k = hits/len(relevant) if relevant else 0.0

    return [precision_k,recall_k]